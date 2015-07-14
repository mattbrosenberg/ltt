
$(document).ready(function(){
  // HELPER FUNCTIONS

  var formatMoney = function(number) {
    number = Number(number);
    return number.toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, '$1,')
  }

  var formatPercent = function(number) {
    number = Number(number);
    return parseFloat(number.toFixed(2))
  }

  // Takes in a list of objects, and a key to sort by.
  // Key param can represent a string or number.
  // Has an optional param [reverse], if true, will return reversed sort.
  var sortBy = function(list, key, reverse) {
      reverse = typeof reverse !== 'undefined' ?  reverse : false;
      return list.sort(function(a,b){
          if (reverse==true) {
              c = a, a = b, b = c; 
          }
          if (a[key] < b[key]) {
              return -1
          }
          else if (a[key] > b[key]) {
              return 1
          }
          else {
              return 0
          }
      });
  }

  var formatTranche = function(json) {
    var formatted_json = "";
    for (var i in json) {
      var item = json[i];
      formatted_json += 
          "<tr class='tranche' id='"+ item['id'] +"'>" +
              "<td>" +
                "<div class='progress'>" + 
                  "<div class='progress-bar progress-bar-success progress-bar-striped active' role='progressbar' aria-valuenow='40' aria-valuemin='0' aria-valuemax='100' style='width:" + 
                    item['funded'] + "%'>" +
                    item['funded'] + "%" +
                  "</div>" + 
                "</div>" + 
              "</td>" +
              "<td>" + formatPercent(item['est_yield']) + "% </td>" +
              "<td> " + item['term'] + "/mo </td>" +
              "<td> $" + formatMoney(item['tranche']) + "</td>" +
              "<td> $" + formatMoney(item['amount_left']) + "</td>" +
              "<td> " + item['time_left'] + " days </td>" +
          "</tr>"
      }
    return formatted_json;
  };

  // END HELPER FUNCTIONS

  $(".filtering").click(function(event){
    event.preventDefault();
  });
  $(".filtering.uni").click(function(event) {
    $(this).parent().find('.filtering').toggleClass("active")
  });
  $(".filtering.multi").click(function(event) {
    $(this).toggleClass("active")
  });



  $("#tranche_loading").hide()
  $(document).ajaxStart(function() {
    $("#tranche_items").css("background-color", "#ddd")
    $("#tranche_div").css("opacity", ".2");
    $("#tranche_loading").show()
  });
  $(document).ajaxStop(function() {
    $("#tranche_items").css("background-color", "white")
    $("#tranche_div").css("opacity", "1");
    $("#tranche_loading").hide()
  });

  var tranches = undefined;
  var ajax_tranches = function(callback){
    var query = [];
    $(".active.filtering").each(function(){
      query.push(this.id);
    });
    query = query.join("+");
    console.log(query);
    $.ajax({
      type: "GET",
      url: '/flex/api/investing/',
      data: query,
      success: function(json){
        $("#tranche_items").html(formatTranche(json['data']));
        tranches = json['data'];
        callback(tranches)
      } //close success json
    }) //close ajax
  };



  ajax_tranches(function(tranches){
    console.log(tranches)
  });

  $(".filtering").click(function(){
    ajax_tranches(function(tranches){
    });
  });

  //SORTING
  $(document).on("click", ".sorting", function(event){
    event.preventDefault();
    key = this.id;
    console.log(key);
    $(this).find(".glyphicon").each(function(){
      if ( $(this).hasClass("glyphicon-sort") ) {
        $(this).removeClass("glyphicon-sort").addClass("glyphicon-sort-by-attributes");
        tranches = sortBy(tranches, key)
        $("#tranche_items").html(formatTranche(tranches));
      }
      else if ( $(this).hasClass("glyphicon-sort-by-attributes") ) {
        $(this).removeClass("glyphicon-sort-by-attributes").addClass("glyphicon-sort-by-attributes-alt");
        tranches = sortBy(tranches, key, true)
        $("#tranche_items").html(formatTranche(tranches));
      }
      else if ( $(this).hasClass("glyphicon-sort-by-attributes-alt") ) {
        $(this).removeClass("glyphicon-sort-by-attributes-alt").addClass("glyphicon-sort-by-attributes");
        tranches = sortBy(tranches, key)
        $("#tranche_items").html(formatTranche(tranches));
      }
    })
  })

  //TRANCHE DETAILS
  $(document).on("click", ".tranche", function(event){
    var footer_height = ($(window).outerHeight() / 2);
// ....
    $("#footer").html("you just clicked on " + this.id + "tranche");
  })



});//end document