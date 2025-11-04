// Ejercicio 6 - Suma de cuadrados con ciclo while
let n = 5;
let resultado = 0;
let i = 1;

while (i <= n) {
    resultado += i * i;
    i++;
}

console.log(`La suma de n_elementos ${n} dio como resultado ${resultado}`);