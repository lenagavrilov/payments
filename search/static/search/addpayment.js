

window.onload = function () {
  document.getElementById('payment_kind').addEventListener('change', validatePaymentKind)
  document.getElementById("check_number").addEventListener("blur", validateCheckNumber);
  document.getElementById('amount').addEventListener("blur", validateAmount);
  document.getElementById('payment_date').addEventListener('blur', validateDate);
  const submitButton = document.getElementById('add_payment');
  //submitButton.disabled = btnState;
} 
//let btnState=true;


function isInt(n) {
  return n % 1 === 0;
}
 
function selectElement(elementID) {
  document.getElementById(elementID).select()
 }

function validatePaymentKind() {
  const payment_kind = document.getElementById('payment_kind');
  document.getElementById('check_error_message').style.display = 'none';
  
  const check_number = document.getElementById('check_number');

  if (payment_kind.value == 1) {
    check_number.style.display = 'inline-block';
    selectElement('check_number');
  } else {
    check_number.style.display = 'none';

    
  }
}


function validateCheckNumber() {
    const check_error_message = document.getElementById('check_error_message');
    
    check_error_message.style.display = 'none';
        
    const checkNumber = document.getElementById("check_number");
    const checkNumAsInt=parseInt(checkNumber.value);
 
    
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
    
    // setTimeout (function() {selectElement('check_number');}, 0);
    selectElement('check_number');
    check_error_message.style.display = 'inline-block';
    check_error_message.innerHTML = errorMsg; 
    btnState = true;
        
    }

    function validateAmount() {
      const amount_error_message = document.getElementById('amount_error_message');
      
      amount_error_message.style.display = 'none';
      let errorMsg = '';    
      const amount = document.getElementById("amount");
  
      amountAsInt = parseInt(amount.value);
      
      let decimalPlaces = 0;
      if (amount.value.includes('.')) {
       decimalPlaces = amount.value.substring(amount.value.indexOf('.') + 1).length;
      } 
           
      if (Number.isInteger(amountAsInt) && (amountAsInt >= 0) && decimalPlaces <=2) {
        btnState = false;
        return;
      }
      if (decimalPlaces >2) {
        errorMsg='The format must be like 123.45';
      
      } else {
        errorMsg='Allows positive numbers only or 0';
  
      }
  //    setTimeout (function() {selectElement('amount');}, 0);
      selectElement('amount');
      amount_error_message.style.display = 'inline-block';
      amount_error_message.innerHTML = errorMsg; 
      btnState = true;
    }


    function validateDate() {
      const date_error_message = document.getElementById('date_error_message');
      
      date_error_message.style.display = 'none';
      payment_date = document.getElementById("payment_date");
      

      let today = new Date();
      let payDate = new Date(payment_date.value);
            
      if (isNaN(payDate.valueOf())) {
        btnState = true;
        date_error_message.style.display = 'inline-block';
        date_error_message.innerHTML = 'Must enter a valid date';
        selectElement('payment_date');
        return;
      }
      if ((today.getFullYear()) !== (payDate.getFullYear())) {
        date_error_message.style.display = 'inline-block';
        date_error_message.style.color = 'green';
        date_error_message.innerHTML = 'Attention: the date is not a current year!';
        
      }
      btnState = false;
      
    }




    



