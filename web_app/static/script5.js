console.log("I am ready! I am ready \u261e")

function f() {
  var btn = document.getElementById("add_csv");
  btn.addEventListener("click", () => {
        document.getElementById("email").style.display = 'none';
        document.getElementById("guess_email").style.display = 'none';
        document.getElementById("csv_file").style.display = '';
    
  }, false);
  
  var btn2 = document.getElementById("guess_btn");
  btn2.addEventListener("click",()=>{
      document.getElementById("email").style.display = 'none';
      document.getElementById("guess_email").style.display = '';
      document.getElementById("csv_file").style.display = 'none';
    
  },false);
  
  var btn3 = document.getElementById("verify_btn");
  btn3.addEventListener("click",()=>{
      document.getElementById("email").style.display = '';
      document.getElementById("guess_email").style.display = 'none';
      document.getElementById("csv_file").style.display = 'none';
    
  },false);
  
}


f();

