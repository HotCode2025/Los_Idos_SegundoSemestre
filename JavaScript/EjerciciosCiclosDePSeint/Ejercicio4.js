// Ejercicio 4 - Promedio y calificación más baja
let calificaciones = [8.5, 7.0, 9.2, 6.8, 8.0, 7.5, 9.8, 6.5, 8.7, 7.2];
let suma = 0;
let min = calificaciones[0];

for (let i = 0; i < calificaciones.length; i++) {
    if (calificaciones[i] < min) {
        min = calificaciones[i];
    }
    suma += calificaciones[i];
}

let promedio = suma / calificaciones.length;

console.log(`La calificación mas baja de todo el grupo es: ${min}`);
console.log(`La calificación promedio de los 10 alumnos es: ${promedio}`);