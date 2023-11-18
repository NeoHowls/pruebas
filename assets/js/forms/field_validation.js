//GESTION DEL RUT - VALIDACIÓN Y FORMATO

//FUNCIÓN DE EVENTO PARA FORMATEAR RUT EN ENTRADA DE TEXTO INPUT
function formatRut(inputElement) {
    let dynamicValue = inputElement.value;

    //Elimina cualquier caracter que no sea un número o la letra 'k' o 'K'
    dynamicValue = dynamicValue.replace(/[^0-9kK]/g, '').toUpperCase();

    // Limitar la cadena a un máximo de 9 caracteres
    if (dynamicValue.length > 9) {
        dynamicValue = dynamicValue.slice(0, 9);

    }

    //Aplicar formato de puntos y guión
    if (dynamicValue.length > 1) {
        let last = dynamicValue.slice(-1);
        dynamicValue = dynamicValue.slice(0, -1);
        dynamicValue = dynamicValue.replace(/\B(?=(\d{3})+\b)/g, '.') + "-" + last;
    }

    // Asignar valor formateado
    inputElement.value = dynamicValue;
}

//MÉTODO DE EVENTO PARA VALIDAR DIGITO VERIFICADOR DE RUT
function validateRut(inputElement, icon) {
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
        icon.classList.replace("checkIconHidden", "checkIcon");
    }
    else {
        icon.classList.replace("checkIcon", "checkIconHidden");
    }
};



//FORMATO CADENA ALFABÉTICA - SOLO LETRAS y ESPACIOS
function formatAlpha(inputElement) {
    let dynamicValue = inputElement.value;

    //Eliminar caracteres numéricos 
    dynamicValue = dynamicValue.replace(/[^a-zA-Z\s]+/g, '').toUpperCase();

    // Limitar la cadena a un máximo de 50 caracteres
    if (dynamicValue.length > 50) {
        dynamicValue = dynamicValue.slice(0, 50);
    }

    //Actualizar valor de elemento
    inputElement.value = dynamicValue;
}
function validateAlpha(inputElement, icon) {
    let dynamicValue = inputElement.value;

    if (dynamicValue.length >= 3) {
        icon.classList.replace("checkIconHidden", "checkIcon");
    }
    else {
        icon.classList.replace("checkIcon", "checkIconHidden");
    }
}



//VALIDACION CORREO ELECTRÓNICO
function validateEmail(inputElement, icon) {
    let dynamicValue = inputElement.value;
    let emailFormat = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

    if(emailFormat.test(dynamicValue)) {
        icon.classList.replace("checkIconHidden", "checkIcon");
    }
    else {
        icon.classList.replace("checkIcon", "checkIconHidden");
    }
}



//VALIDACION DE CONTRASEÑA
function validatePassword(inputElement, icon) {
    let dynamicValue = inputElement.value;

    //Mínimo 8 caracteres
    let lengthValue = dynamicValue.length >= 8 ? true : false;
    // Debe contener al menos una letra y al menos un número
    let letterValue = /[a-zA-Z]/.test(dynamicValue);
    let numberValue = /[0-9]/.test(dynamicValue);

    if(lengthValue && letterValue && numberValue) {
        icon.classList.replace("checkIconHidden", "checkIcon");
    }
    else {
        icon.classList.replace("checkIcon", "checkIconHidden");
    }
}

//Función para ocultar / mostrar contraseña dinámicamente
function showHide(inputElement, eyeicon) {
    if(inputElement.type == "password") {
        inputElement.type = "text";
        eyeicon.classList.replace("fa-eye-slash","fa-eye");
        eyeicon.setAttribute("style", "color:#0080ff");
    }
    else {
        inputElement.type = "password";
        eyeicon.classList.replace("fa-eye","fa-eye-slash");
        eyeicon.removeAttribute("style");
    }
}



//CONFIRMAR CONTRASEÑA
//Validación de coincidencia
function validateConfirmPassword(password1, password2, icon) {
    let password = password1;
    let confirm_password = password2.value;

    if(password == confirm_password) {
        icon.classList.replace("checkIconHidden", "checkIcon");
    }
    else {
        icon.classList.replace("checkIcon", "checkIconHidden");
    }
}



//FORMATO TELÉFONO (Sólo dígitos) 8
function formatNumber(inputElement) {
    let dynamicValue = inputElement.value;

    //Eliminar caracteres no numéricos 
    dynamicValue = dynamicValue.replace(/[^0-9]/g, '');

    // Limitarun máximo de 8 caracteres
    if (dynamicValue.length > 8) {
        dynamicValue = dynamicValue.slice(0, 8);
    }

    //Actualizar valor de elemento
    inputElement.value = dynamicValue;
}
//VALIDACION TELEFONO
function validateNumber(inputElement, icon) {
    let dynamicValue = inputElement.value;

    if (dynamicValue.length >= 8 && /^[0-9]+$/.test(dynamicValue)) {
        icon.classList.replace("checkIconHidden", "checkIcon");
    }
    else {
        icon.classList.replace("checkIcon", "checkIconHidden");
    }
}



//Evento load cuando se cargue el DOM para los checks de validaciones
window.addEventListener("load", async () => {
    validateRut(inputRut, checkRut);
    validateAlpha(inputName, checkName);
    validateAlpha(inputLastName, checkLastName);
    validateEmail(inputEmail, checkEmail);
    validatePassword(inputPassword, checkPassword);
    validateNumber(inputNumber, checkNumber);
});



//------------------------------------------------------------------
//------------------------------------------------------------------
//------------------------------------------------------------------


/*SELECCION DE ELEMENTO Y APLICACIÓN DE EVENTOS*/
//RUT
const inputRut = document.getElementById("input-rut");
const checkRut = document.getElementById("check-rut");
//Evento formato
inputRut.addEventListener('input', ()=> {
    formatRut(inputRut);
});
//Evento validación
inputRut.addEventListener('blur', ()=> {
    validateRut(inputRut, checkRut);
});


//NOMBRE
const inputName = document.getElementById("input-name");
const checkName = document.getElementById("check-name");
//Evento formato
inputName.addEventListener('input', ()=> {
    formatAlpha(inputName);
})
//Evento validación
inputName.addEventListener('blur', ()=> {
    validateAlpha(inputName, checkName);
});


//APELLIDO
const inputLastName = document.getElementById("input-lastname");
const checkLastName = document.getElementById("check-lastname");
//Evento formato
inputLastName.addEventListener('input', ()=> {
    formatAlpha(inputLastName);
})
//Evento validación
inputLastName.addEventListener('blur', ()=> {
    validateAlpha(inputLastName, checkLastName);
});


//CORREO ELECTRONICO
const inputEmail = document.getElementById("input-email");
const checkEmail = document.getElementById("check-email");
//Evento validación
inputEmail.addEventListener('blur', ()=> {
    validateEmail(inputEmail, checkEmail);
})


//CONTRASEÑA
const inputPassword = document.getElementById("input-password");
const eyeicon = document.getElementById("eye-slash-icon");
const checkPassword = document.getElementById("check-password");
//Evento validación
inputPassword.addEventListener('blur', ()=> {
    validatePassword(inputPassword, checkPassword);
})
//Mostrar y/o ocultar contraseña
eyeicon.addEventListener("click", ()=>{
    showHide(inputPassword, eyeicon);
});

//CONFIRMAR CONTRASEÑA
const inputConfirmPassword = document.getElementById("input-confirm_password")
const checkConfirmPassword = document.getElementById("check-confirm_password");
//Evento validación
inputConfirmPassword.addEventListener('blur', ()=> {
    validateConfirmPassword(inputPassword.value, inputConfirmPassword, checkConfirmPassword);
})

//TELEFONO
const inputNumber = document.getElementById("input-number");
const checkNumber = document.getElementById("check-number");
//Evento formato
inputNumber.addEventListener('input', ()=> {
    formatNumber(inputNumber);
})
//Evento validación
inputNumber.addEventListener('blur', ()=> {
    validateNumber(inputNumber, checkNumber);
});