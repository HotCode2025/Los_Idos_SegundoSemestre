// Ejercicio 10 - Máximo y mínimo de N números
let numeros = [15, 8, 23, 4, 42, 19, 7, 31, 11, 28];
let max = numeros[0];
let min = numeros[0];

for (let i = 1; i < numeros.length; i++) {
    if (numeros[i] > max) {
        max = numeros[i];
    } else if (numeros[i] < min) {
        min = numeros[i];
    }
}

console.log(`El numero máximo fue ${max}`);
console.log(`El numero mínimo fue ${min}`);