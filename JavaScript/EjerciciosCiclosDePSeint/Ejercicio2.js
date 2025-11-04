// Ejercicio 2 - Suma de pares e impares entre 1 y 50
let pares = 0;
let impares = 0;

for (let i = 2; i <= 49; i++) {
    if (i % 2 === 0) {
        pares += i;
    } else {
        impares += i;
    }
}

console.log(`La suma de pares es: ${pares}`);
console.log(`La suma de impares es: ${impares}`);