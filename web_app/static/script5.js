console.log("I am ready! I am ready \u261e")


function f() {
  var btn = document.getElementById("add_csv");
  btn.addEventListener("click", () => {
        document.getElementById("email").style.display = 'none';
        document.getElementById("guess_email").style.display = 'none';
        document.getElementById("csv_file").style.display = '';
        document.getElementById("guess_file").style.display = 'none';
    
  }, false);
  
  var btn2 = document.getElementById("guess_btn");
  btn2.addEventListener("click",()=>{
      document.getElementById("email").style.display = 'none';
      document.getElementById("guess_email").style.display = '';
      document.getElementById("csv_file").style.display = 'none';
      document.getElementById("guess_file").style.display = 'none';
    
  },false);
  
  var btn3 = document.getElementById("verify_btn");
  btn3.addEventListener("click",()=>{
      document.getElementById("email").style.display = '';
      document.getElementById("guess_email").style.display = 'none';
      document.getElementById("csv_file").style.display = 'none';
      document.getElementById("guess_file").style.display = 'none';
    
  },false);
  
  var btn4 = document.getElementById("guess_file_btn");
  btn4.addEventListener("click",()=>{
        document.getElementById("email").style.display = 'none';
        document.getElementById("guess_email").style.display = 'none';
        document.getElementById("csv_file").style.display = 'none';
        document.getElementById("guess_file").style.display = '';  
  },false);
  
}


f();

// $(document).ready(function(){
    
//     /* The following code is executed once the DOM is loaded */

//     /* This flag will prevent multiple comment submits: */
//     var working = false;
//     $("#email").submit(function(e){
//       e.preventDefault();
//     $.ajax({
//          type: 'POST',
//          url: $("#email").attr("action"),
//         data: $("#email").serialize(), 
//         success: function(response) {
//           alert(JSON.stringify(response));
//         },
//         error: function(xhr, status, error) {
//   alert(xhr.responseText);
// }
//      });
// });



//  $("guess_email").submit(function(e){
//       e.preventDefault();
//       alert($("#guess_email").attr("action"));
//     $.ajax({
//          type: 'POST',
//          url: $("#guess_email").attr("action"),
//         data: $("#guess_email").serialize(), 
//         success: function(response) {
//           alert(JSON.stringify(response));
//         },
//         error: function(xhr, status, error) {
//   alert(xhr.responseText);
// }
//      });
// });



//  $("csv_file").submit(function(e){
//       e.preventDefault();
//       var formData = new FormData('hello');
//     $.ajax({
//          type: 'POST',
//          url: $("#csv_file").attr("action"),
//         data: formData,
//         async: false, 
//         success: function(response) {
//           alert(JSON.stringify(response));
//         },
//         error: function(xhr, status, error) {
//   alert(xhr.responseText);
// }
//      });
// });
//});