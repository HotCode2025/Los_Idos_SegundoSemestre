// Ejercicio 9 - Serie alternante
let n = 5;
let i = 1;
let total = 0;
let signo = 1;

do {
    total += signo / i;
    signo *= -1;
    i++;
} while (i <= n);

console.log(`El resultado final es ${total}`);