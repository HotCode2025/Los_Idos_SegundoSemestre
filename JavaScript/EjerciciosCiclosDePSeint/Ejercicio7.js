// Ejercicio 7 - Análisis de números pares e impares
let elementos_n = 10;
let i = 1;
let suma_pares = 0;
let suma_impares = 0;
let cantidad_pares = 0;
let cantidad_impares = 0;

while (i <= elementos_n) {
    if (i % 2 === 0) {
        suma_pares += i;
        cantidad_pares++;
    } else {
        suma_impares += i;
        cantidad_impares++;
    }
    i++;
}

let promedio_impares = suma_impares / cantidad_impares;

console.log("Analisis del resultado final arrojó");
console.log(`Suma de los pares sumados: ${suma_pares}`);
console.log(`Cantidad de números pares encontrados: ${cantidad_pares}`);
console.log(`Promedio de números impares de la lista: ${promedio_impares}`);