function validateForm() {
  var name = document.myForm.name.value;
  var password = document.myForm.pass.value;

  if (name == null || name == "") {
    alert("Username can't be blank! Please try a valid username");
    return false;
  } else if (password.length < 6) {
    alert("Password are at least 6 characters long! Please try again");
    return false;
  } else if (!/^(?=.*[\d])(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,}$/.test(password)) {
    alert(
      "Password must contain atleast one numeric and one special character!"
    );
    return false;
  }

  return true;
}

function login() {
  if (validateForm()) {
    alert("Logged in successfully!");
  }
}
