// Ejercicio 11 - Serie de Fibonacci
let n = 10;
let fibo_1 = 0;
let fibo_2 = 1;

console.log("Serie de Fibonacci:");
for (let i = 1; i <= n; i++) {
    console.log(fibo_1);
    let suma = fibo_1 + fibo_2;
    fibo_1 = fibo_2;
    fibo_2 = suma;
}