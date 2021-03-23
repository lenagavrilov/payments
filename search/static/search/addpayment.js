

window.onload = function () {
  document.getElementById("check_number").addEventListener("blur", validateCheckNumber);
  const submitButton = document.getElementById('add_payment');
  submitButton.disabled = btnState;
} 
let btnState=true;

function isInt(n) {
  return n % 1 === 0;
}

function validateCheckNumber() {
    const error_message = document.getElementById('check_error_message');
    
    error_message.style.display = 'none';
        
    const checkNumber = document.getElementById("check_number");
    const checkNumAsInt=parseInt(checkNumber.value);
    
    console.log(isInt(checkNumber.value));
    
    let errorMsg="";
    if (isInt(checkNumber.value) && checkNumAsInt > 0) {
      btnState = false;
      return;
    }
    if (isNaN(checkNumAsInt) || !isInt(checkNumber.value)) {
      errorMsg= 'Check number must be a round number';
    }
    else{
      errorMsg='Must be bigger than 0';
    }
        error_message.style.display = 'inline-block';
        error_message.innerHTML = errorMsg;  
    }
 

