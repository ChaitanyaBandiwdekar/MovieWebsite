function validateForm() {
	var name = document.myForm.name.value;  
	var password = document.myForm.pass.value;  
	var email = document.myForm.email.value;
	  
	if (name==null || name==""){  
		alert("Name can't be blank");  
		return false;  
	}
	
	else if (!/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email)){
		alert("You have entered an invalid email address!");
		return false;
	}
	
	else if(!radioButtonValidate()){
		alert('Atleast one gender should be selected!');
		return false;
	}
	
	else if(password.length<6){  
		alert("Password must be at least 6 characters long.");  
		return false;  
	} 
	
	else if(!/^(?=.*[\d])(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,}$/.test(password)){
		alert("Password must contain atleast one numeric and one special character!");  
		return false;
	}
	
	else if(!document.myForm.TnC.checked){
		alert('You must agree to the terms first.');
		return false;
	}
	
}

function radioButtonValidate(){
	var radios = document.getElementsByName("gender");
    var formValid = false;

    var i = 0;
    while (!formValid && i < radios.length) {
        if (radios[i].checked) formValid = true;
        i++;        
    }
	
    return formValid;
}