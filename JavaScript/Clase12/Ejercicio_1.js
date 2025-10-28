// Ejercicio 1: Función que valide una contraseña (mínimo 8 caracteres, 1 número, 1 mayúscula)

function validatePassword(password) {

    if (password.length < 8) {
        return false;
    }
    
    let tieneNumero = false;
    let tieneMayus = false;
    
    for (let i = 0; i < password.length; i++) {
        const char = password[i];
        
        if (char >= '0' && char <= '9') {
            tieneNumero = true;
        }
        
        if (char >= 'A' && char <= 'Z') {
            tieneMayus = true;
        }
    }
    
    return tieneNumero && tieneMayus;
}

console.log(validatePassword("batata01"));
console.log(validatePassword("Batata"));
console.log(validatePassword("Batata1"));
console.log(validatePassword("Batata01"));