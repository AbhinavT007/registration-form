function validateEmail() {
    let email = document.getElementById("email").value;
    let errorMessage = document.getElementById("email-error");
    
    // Check if email contains '@'
    if (!email.includes("@")) {
        errorMessage.textContent = "Email must contain @";
        return false; // Prevent form submission
    } else {
        errorMessage.textContent = "";
        return true;
    }
}
