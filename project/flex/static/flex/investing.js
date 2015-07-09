
$(document).ready(function(){

  var format_tranche_items = function(json) {
    var formatted_json = "";
    for (var i in json) {
      var item = json[i];
      formatted_json += 
          "<tr>" +
          //   "<td>" +
          //     "<div class='investAmountInput'>$0</div>" +
          //   "</td>" +
              "<td>" +
                "<div class='progress'>" + 
                  "<div class='progress-bar progress-bar-success progress-bar-striped active' role='progressbar' aria-valuenow='40' aria-valuemin='0' aria-valuemax='100' style='width:" + 
                    item['percent_residuals_funded'] + "%'>" +
                    item['percent_residuals_funded'] + "%" +
                  "</div>" + 
                "</div>" + 
              "</td>" +
              "<td>" + item['days_to_auction'] + " days </td>" +
              "<td> $" + item['residual_investment'] + "</td>" +
              "<td> " + item['dated_date'] + "</td>" +
              "<td> " + item['maturity'] + "</td>" +
          "</tr>"
      }
    return formatted_json;
  };//end format_tranche_items


  $(".sorting").click(function(event){
    event.preventDefault();
  });
  $(".sorting.uni").click(function(event) {
    $(this).parent().find('.sorting').toggleClass("active")
  });
  $(".sorting.multi").click(function(event) {
    $(this).toggleClass("active")
  });

  $(".sorting").click(function(){
    var query = [];
    $(".active.sorting").each(function(){
      query.push(this.id);
    });
    query = query.join("+");
    $.ajax({
      type: "GET",
      url: '/flex/api/investing/',
      data: query,
      success: function(json){
        $("#tranche_items").html(format_tranche_items(json['data']));
      } //close success json
    }) //close ajax
  });

});//end document