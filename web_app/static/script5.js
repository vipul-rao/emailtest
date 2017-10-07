console.log("I am ready! I am ready \u261e")

function f() {
  let myStatus = true;
  var btn = document.getElementById("add_csv");
  
  btn.addEventListener("click", () => {
    myStatus = !myStatus; //here the value is inverted only with the ! (not)
    if(!myStatus){
        btn.innerHTML = "enter email"
        document.getElementById("email").style.display = 'none';
        document.getElementById("csv_file").style.display = '';
    }else{
        btn.innerHTML = "upload csv"
        document.getElementById("csv_file").style.display = 'none';
        document.getElementById("email").style.display = '';
    }
    console.log(myStatus);
  }, false);
}

f();
