//RUT
function formValidateRut(inputElement) {
    let rut = inputElement.value;
    let checkDigit = rut.slice(-1);
    let cleanRut = rut.slice(0, -1).replace(/\D/g, '');
    
    let array = cleanRut.split('').reverse();
    let acumulator = 0;
    let multiplicator = 2;


    for(let number of array) {
        acumulator += parseInt(number) * multiplicator;
        multiplicator++;
        //Necesitamos resetear el multiplicador a 2 , ya que la fórmula indica que el incremento es hasta el 7
        if(multiplicator == 8) {
            multiplicator = 2;
        }
    }
    
    //Aquí obtenemos el resto al dividir la suma total por 11
    let digit = 11 - (acumulator % 11);

    //Si el dígito verificador es 11, se convierte a 0
    if(digit == 11) {
        digit = '0';
    }

    //Si el dígito verificador es 10, se convierte a k
    else if(digit == 10) {
        digit = 'K';
    }

    if (digit == checkDigit && cleanRut.length >=8) {
        return true;
    }
    else {
        return false;
    }
};


//NOMBRE, APELLIDO
function formValidateAlpha(inputElement) {
    let dynamicValue = inputElement.value;
    let format = /^[a-zA-Z\s]+$/;


    if (dynamicValue.length >= 3 && format.test(dynamicValue) == true) {
       return true;
    }
    else {
        return false;
    }
}


//EMAIL
function formValidateEmail(inputElement) {
    let dynamicValue = inputElement.value;
    let format = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

    if(format.test(dynamicValue)) {
        return true;
    }
    else {
        return false;
    }
}


//CONTRASEÑA
function formValidatePassword(inputElement) {
    let dynamicValue = inputElement.value;
    //Mínimo 8 caracteres
    let lengthValue = dynamicValue.length >= 8 ? true : false;
    // Debe contener al menos una letra y al menos un número
    let letterValue = /[a-zA-Z]/.test(dynamicValue);
    let numberValue = /[0-9]/.test(dynamicValue);

    if(lengthValue && letterValue && numberValue) {
        return true
    }
    else {
        return false
    }
}


//CONFIRMAR CONTRASEÑA
function formConfirmPassword(inputElement1, inputElement2) {
    let password1 = inputElement1.value;
    let password2 = inputElement2.value;

    if (password1 == password2) {
        return true
    }
    else {
        return false
    }
}


//TELEFONO
function formValidateNumber(inputElement) {
    let dynamicValue = inputElement.value;

    if (dynamicValue.length >= 8 && /^[0-9]+$/.test(dynamicValue)) {
        return true
    }
    else {
        return false
    }
}


//SELECTS
function formValidateSelect(selectElement) {
    let dynamicValue = selectElement.value;

    if (dynamicValue != 0) {
        return true
    }
    else {
        return false
    }
}

//VALIDACION DE FORMULARIO COMPLETO ANTES DE ENVIAR AL SERVIDOR
function formValidation() {
    //let rut = document.getElementById('input-rut');
    //let name = document.getElementById('input-name');
    //let lastname = document.getElementById('input-lastname');
    //let email = document.getElementById('input-email');
    //let password = document.getElementById('input-password');
    //let confirm_password = document.getElementById('input-confirm_password');
    //let number = document.getElementById('input-number');
    //let profile = document.getElementById('selectProfile');
    //let region = document.getElementById('selectRegion');
    //let comune = document.getElementById('selectComune');
    //let station = document.getElementById('selectStation');

    if(formValidateRut(inputRut) && formValidateAlpha(inputName) && formValidateAlpha(inputLastName) && formValidateEmail(inputEmail) && formValidatePassword(inputPassword) && formConfirmPassword(inputPassword, inputConfirmPassword) && formValidateNumber(inputNumber) && formValidateSelect(selectProfile) && formValidateSelect(selectRegion) && formValidateSelect(selectComune) && formValidateSelect(selectStation)) {
        console.log("Creación de usuario correcta");
        return true
    }
}

//Selección del formulario
const signupForm = document.getElementById("signup-form");
const signupButtonForm = document.getElementById("signup-form-button");

signupForm.addEventListener("submit", (event) => {
    if (!formValidation()) {
        event.preventDefault();
        console.log("Creación de usuario incorrecta");
    }
})
