// Ejercicio 5 - Suma de cuadrados
let N = 5;
let suma = 0;

for (let i = 1; i <= N; i++) {
    suma += (i * i);
}

console.log(`S = 1 + 4 + 9 + ... + ${N}² = ${suma}`);