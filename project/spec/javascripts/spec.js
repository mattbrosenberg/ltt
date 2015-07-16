// describe("Checking matched elements in DOM.", function() {
//   it("should check for elements in DOM.", function() {
//     expect($('#trade_history')).toBeInDOM();
//   });
// });

// describe("Checking click triggered on trade_history.", function() {
//   it("Should check for click on trade_history.", function() {
//     var spyEvent = spyOnEvent('#trade_history', 'click');
//     $('#trade_history').click()
//     expect('click').toHaveBeenTriggeredOn('#trade_history');
//     expect(spyEvent).toHaveBeenTriggered();
//   }); // end it
// }); // describe

// describe("Checking AJAX request to get portfolio.", function() {
//   function getPortfolio() {
//       $.ajax({
//           type: "GET",
//           url: "/flex/portfolio/investments",
//           contentType: "application/json; charset=utf-8",
//           dataType: "json",
//       });
//
//   }
//
//   it("Should make an AJAX request to the correct URL.", function() {
//       spyOn($, "ajax");
//       getPortfolio();
//       expect($.ajax.mostRecentCall["url"]).toEqual("/flex/portfolio/investments");
//   });
// });

// describe("Checking that callback request was executed, upon AJAX request completing successfully.", function() {
//   function getPortfolio(callback) {
//       $.ajax({
//           type: "GET",
//           url: "/flex/portfolio/investments",
//           contentType: "application/json; charset=utf-8",
//           dataType: "json",
//           success: callback,
//       });
//   }
//
//   it("Should execute the callback function on success.", function () {
//       spyOn($, "ajax").andcallFake(function(options) {
//           options.success();
//       });
//       var callback = jasmine.createSpy();
//       getPortfolio(callback);
//       expect(callback).toHaveBeenCalled();
//   });
// });

// describe("Checking for successful ajax request on get portfolio.", function() {
//   var portfolio, request;
//   var onSuccess, onFailure;
//
//   beforeEach(function() {
//     jasmine.Ajax.install();
//
//     onSuccess = jasmine.createSpy('onSuccess');
//     onFailure = jasmine.createSpy('onFailure');
//
//     function getPortfolio() {
//         $.ajax({
//             type: "GET",
//             url: "/flex/portfolio/investments",
//             contentType: "application/json; charset=utf-8",
//             dataType: "json",
//             onSuccess: onSuccess,
//             onFailure: onFailure,
//         }); // ajax
//
//     } // getPortfolio
//
//     request = jasmine.Ajax.requests.mostRecent();
//     expect($.ajax.mostRecentCall["url"]).toEqual("/flex/portfolio/investments");
//   });// beforeEach
//
//   describe("on success", function() {
//     beforeEach(function() {
//       request.respondWith(TestResponses.success);
//     }); // end beforeEach
//
//     it("calls onSuccess with a list of investments", function() {
//       expect(onSuccess).toHaveBeenCalled();
//
//       var successArgs = onSuccess.calls.mostRecent().args[0];
//
//       expect(successArgs.length).toEqual(1);
//       expect(successArgs[0]).toEqual(jasmine.any(Venue));
//     }); // end it
//   }); // end describe
// }); // end describe








//   it("can perform a successful ajax request on portfolio.html", function() {
//     var asyncCallComplete, result,
//       _this = this;
//     // asyncCallComplete is set to true when the ajax call is complete
//     asyncCallComplete = false;
//
//     // result stores the result of the successful ajax call
//     result = null;
//
//     // SECTION 1 - call asynchronous function
//     runs(function() {
//       return $.ajax('/flex/templates/flex/portfolio.html', {
//         type: 'GET',
//         success: function(data) {
//           asyncCallComplete = true;
//           result = data;
//         },
//         error: function() {
//           asyncCallComplete = true;
//         }
//       });
//     });
//
//     // SECTION 2 - wait for the asynchronous call to complete
//     waitsFor(function() {
//       return asyncCallComplete !== false;
//     });
//
//     // SECTION 3 - perform tests
//     return runs(function() {
//       return expect(result).not.toBeNull();
//     });
//   });
// });


define(["flex/portfolio/investments"], function(Investments) {
  describe("")
})
