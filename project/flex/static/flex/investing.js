
$(document).ready(function(){

  // Takes in a list of objects, and a key to sort by.
  // Key param can represent a string or number.
  // Has an optional param [reverse], if true, will return reversed sort.
  var sorted = function(list, key, reverse) {
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

  var format_tranche_items = function(json) {
    var formatted_json = "";
    for (var i in json) {
      var item = json[i];
      formatted_json += 
          "<tr>" +
              "<td>" +
                "<div class='progress'>" + 
                  "<div class='progress-bar progress-bar-success progress-bar-striped active' role='progressbar' aria-valuenow='40' aria-valuemin='0' aria-valuemax='100' style='width:" + 
                    item['funded'] + "%'>" +
                    item['funded'] + "%" +
                  "</div>" + 
                "</div>" + 
              "</td>" +
              "<td>" + item['est_yield'] * 100 + "% </td>" +
              "<td> " + item['term'] + "/mo </td>" +
              "<td> $" + item['tranche'] + "</td>" +
              "<td> $" + item['amount_left'] + "</td>" +
              "<td> " + item['time_left'] + " days </td>" +
          "</tr>"
      }
    return formatted_json;
  };//end format_tranche_items

  $(".filtering").click(function(event){
    event.preventDefault();
  });
  $(".filtering.uni").click(function(event) {
    $(this).parent().find('.filtering').toggleClass("active")
  });
  $(".filtering.multi").click(function(event) {
    $(this).toggleClass("active")
  });


  var tranches = undefined;
  var ajax_tranches = function(callback){
    var query = [];
    $(".active.filtering").each(function(){
      query.push(this.id);
    });
    query = query.join("+");
    $.ajax({
      type: "GET",
      url: '/flex/api/investing/',
      data: query,
      success: function(json){
        $("#tranche_items").html(format_tranche_items(json['data']));
        tranches = json['data'];
        callback(tranches)
      } //close success json
    }) //close ajax
  };
  ajax_tranches(function(tranches){
  });
  $(".filtering").click(function(){
    ajax_tranches(function(tranches){
    });
  });

  //table header sorting
  $(document).on("click", ".sorting", function(event){
    event.preventDefault();
    key = this.id;
    console.log(key);
    $(this).find(".glyphicon").each(function(){
      if ( $(this).hasClass("glyphicon-sort") ) {
        $(this).removeClass("glyphicon-sort").addClass("glyphicon-sort-by-attributes");
        tranches = sorted(tranches, key)
        $("#tranche_items").html(format_tranche_items(tranches));
      }
      else if ( $(this).hasClass("glyphicon-sort-by-attributes") ) {
        $(this).removeClass("glyphicon-sort-by-attributes").addClass("glyphicon-sort-by-attributes-alt");
        tranches = sorted(tranches, key, true)
        $("#tranche_items").html(format_tranche_items(tranches));
      }
      else if ( $(this).hasClass("glyphicon-sort-by-attributes-alt") ) {
        $(this).removeClass("glyphicon-sort-by-attributes-alt").addClass("glyphicon-sort-by-attributes");
        tranches = sorted(tranches, key)
        $("#tranche_items").html(format_tranche_items(tranches));
      }
    })
  })

});//end document