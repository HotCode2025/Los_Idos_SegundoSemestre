// Ejercicio 12 - Sumatoria con factorial y potencia
let n_serie = 5;
let x = 2;
let total_sumatoria = 0;
let factorial = 1;

for (let i = 1; i <= n_serie; i++) {
    if (i === 1) {
        factorial = 1;
        total_sumatoria = 1 + x;
    } else {
        factorial *= i;
        total_sumatoria += Math.pow(x, i) / factorial;
    }
}

console.log(`El resultado de la sumatoria es ${total_sumatoria}`);