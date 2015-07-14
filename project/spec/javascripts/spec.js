describe("Testing price variable.", function() {
  var json_data = function(json) {
    for (var key in json) {

      var value = json[key];
      console.log(value['price']);

      it("Price must be greater than zero.", function() {
        expect(value['price']).toBeGreaterThan(0);
      });
    } //end for
  } // end json
});
