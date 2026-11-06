document.addEventListener("DOMContentLoaded", ()=>{
  const passwordField = document.querySelector("#update_password");
  const repeatPasswordField = document.querySelector("#repeat_password");

  const checkPasswordValidity = () => {
    const p = passwordField.value;
    const r = repeatPasswordField.value;

    if(p.length < 5) {
      passwordField.setCustomValidity("Password must be at least 5 characters long");
    } else if (p == "12345") {
      passwordField.setCustomValidity("That's the kind of password an idiot would have on his luggage!");
    } else {
      passwordField.setCustomValidity("");
    }
    
    if(!passwordField.checkValidity()) {
      repeatPasswordField.setCustomValidity("");
      repeatPasswordField.reportValidity();
      passwordField.reportValidity();
      return;
    } 
    
    passwordField.reportValidity();

    if(p == r) {
      repeatPasswordField.setCustomValidity("");
    } else {
      repeatPasswordField.setCustomValidity("Password doesn't match");
    }
    repeatPasswordField.reportValidity();
  }

  passwordField.addEventListener("input", checkPasswordValidity);
  repeatPasswordField.addEventListener("input", checkPasswordValidity);
})