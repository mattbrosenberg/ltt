  $(document).ready(function(){
      event.preventDefault();
      $.ajax({
      	type:"GET",
      	url: '/flex/portfolio/investments',
      	success: function(json){
      		$("#portfolio_head").html("<tr><th>Contract</th><th>Price paid</th><th>Value</th><th>Purchase Time</th><th>Maturity Date</th></tr>");
      		var data = eval(json);
      		for (var key in data) {
      			var value = data[key];
      			for (x in value) {
      				$("#portfolio_items").append("<tr><td><a href ='#'>" + value[x]['contract'] +"</a></td><td> $" + value[x]['price'] + "</td><td>$" + value[x]['price'] + "</td><td>" + value[x]['purchase_date'] + "</td><td>" + value[x]['maturity'] + "</td>>/tr>")
      			}
      		}
      		// $("#portfolio_items").html("<tr><td>" + )
      	}
      })

      $("#trade_history").on("click", function(event){
    event.preventDefault();
    $.ajax({
      type: "GET",
      url: '/flex/portfolio/history',
      success: function(json){
      	$("#portfolio_head").html("<tr><th>Contract</th><th>Buyer</th><th>Seller</th><th>Sale Proceeds</th><th>Sale Time</th></tr>");
        $('#potfolio_head').empty();
        $('#portfolio_items').empty();
        var data = eval(json);
        for (var key in data) {
        	var value = data[key];
        	for (x in value) {
        		$("#portfolio_items").append("<tr> <td>" + value[x]['id'] + "</td> <td>" + value[x]['buyer'] + "<td>" + value[x]['seller'] + "</td> <td> $" + value[x]['proceeds'] + "</td> <td>" + value[x]['time'] + "</td> </tr>"  )
        	}
        }
    }
    });
    });    



});  
