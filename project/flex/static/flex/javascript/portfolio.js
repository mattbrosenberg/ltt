  $(document).ready(function(){

    var json_data = function(json) {
      var formatted_json = "";
          for (var key in json) {
            var value = json[key];
            formatted_json +=
                  "<tr data-id='" + value['contract'] +"'><td><button type='button' class='btn btn-primary' id=button"+value['contract'] + ">"+ value['contract']+"</button> </td>" +
                  "<td> $" + value['price']+ "</td>"+
                  "<td>$" + value['price'] + "</td>" +
                  "<td>" + value['purchase_date'] + "</td>"+
                  "<td>" + value['maturity'] + "</td>" +"</tr>"+
                  "<tr><td colspan='5' id='info'><div class='collapse details' data-id='" + value['contract'] +"'>stuff here</div></td></tr>"
          }
    return formatted_json;
  };

    var formatted_cashflows = function(json) {
      var formatted_json =

      "<h2>Details</h2>" +
      "<h3> Average annualized return on investment: </h3>" +
      "<p>" + json['average_return'] + "%</p>" +
      "<h3>Cashflows received since contract's purchase: </h3>" +
              "<table class='table table-hover table-condensed' id='cashflow_table'>" +
          "<tr>" +
            "<th>Date</th>"+
            "<th>Amount ($)</th></tr>" ;
      for (var key in json['cashflows']) {
        var value = json['cashflows'][key];
        formatted_json +=
          "<tr>" +
            "<td>" + value['date'] + "</td>"+
            "<td>" + value['amount'] + "</td></tr>"
                  }
        formatted_json += "<tr>" +
        "<td> Total </td>" +
        "<td>" + json['total'] + "</td>" +
        "</table>"
      return formatted_json;
    };

      event.preventDefault();
      $.ajax({
      	type:"GET",
      	url: '/flex/portfolio/investments',
      	success: function(json){
      		$("#portfolio_head").html("<tr><th>Contract</th><th>Price paid</th><th>Value</th><th>Purchase Time</th><th>Maturity Date</th></tr>");
          $("#portfolio_items").html(json_data(json['investments']));
          $(".btn-primary").each(function(){
            $(this).click(function() {
              var target_id = $( $(this).closest('tr')[0] ).attr('data-id');
              $.ajax({
                type:"GET",
                url: '/flex/portfolio/contract',
                data: {'contract' : target_id},
                success: function(json){
                  $('[data-id="'+ target_id +'"].collapse').html(formatted_cashflows(json['data']));
                  $('[data-id="'+ target_id +'"].collapse').collapse('toggle');
                }
              })
            })
          })
        }
      })

      $('.nav-sidebar li').click(function(event) {
          $('.nav-sidebar li.active').removeClass('active');
          var $this = $(this);
          if (!$this.hasClass('active')) {
              $this.addClass('active');
          }
          event.preventDefault();
      });

      $("#portfolio").on("click", function(event){
        event.preventDefault();
        window.location.href="/flex/portfolio"
      })

    //   $("#trade_history").on("click", function(event){
    // event.preventDefault();
    // $.ajax({
    //   type: "GET",
    //   url: '/flex/portfolio/history',
    //   success: function(json){
    //   	$("#portfolio_head").html("<tr><th>Date</th><th>Category</th><th>Description</th><th>Debit</th><th>Credit</th></tr>");
    //     $('#portfolio_items').empty();
    //     var data = eval(json);
    //     for (var key in data) {
    //     	var value = data[key];
    //     	for (x in value) {
    //     		$("#portfolio_items").append("<tr> <td>" + value[x]['id'] + "</td> <td>" + value[x]['buyer'] + "<td>" + value[x]['seller'] + "</td> <td> $" + value[x]['proceeds'] + "</td> <td>" + value[x]['time'] + "</td> </tr>"  )
    //     	}
    //     }
    // }
    // });
    // });

    var formatted_transactions = function(json) {
      var formatted_json = "";
          for (var key in json) {
            var value = json[key];
            formatted_json +=
                  "<tr>" +
                  "<td>" + value['date']+ "</td>"+
                  "<td>" + value['category'] + "</td>" +
                  "<td colspan='2' style='width:40%'>" + value['description'] + "</td>"+
                  "<td>" + value['amount'] + "</td>" +"</tr>"
          }
          formatted_json +=
                "<tr>" +
                "<td colspan='4'> Available Balance </td>" +
                "<td></td></tr>"
    return formatted_json;
    }

      $("#trade_history").on("click", function(event){
        event.preventDefault();
        $.ajax({
        type: "GET",
        url: '/flex/portfolio/activity',
        success: function(json){
          $("#portfolio_head").html("<tr><th>Date</th><th>Category</th><th colspan='2' style='width:40%'>Description</th><th>Amount ($)</th></tr>");
          $("#portfolio_items").html(formatted_transactions(json['transactions']));
          console.log(json)
        }
      });
    });
});
