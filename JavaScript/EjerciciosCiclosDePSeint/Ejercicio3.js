// Ejercicio 3 - Contador de positivos, negativos y neutros
let numeros = [5, -3, 0, 8, -1, 0, 2, -7, 4, -2];
let pos = 0;
let neg = 0;
let neu = 0;

for (let i = 0; i < numeros.length; i++) {
    let n = numeros[i];
    
    if (n > 0) {
        pos++;
    } else if (n < 0) {
        neg++;
    } else {
        neu++;
    }
}

console.log(`Ingresaste ${pos} números positivos.`);
console.log(`Ingresaste ${neg} números negativos.`);
console.log(`Ingresaste ${neu} números neutros.`);