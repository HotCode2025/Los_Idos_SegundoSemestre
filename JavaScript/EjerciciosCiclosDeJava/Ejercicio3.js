// Ejercicio 3 - Ciclo For con Break
console.log("Palabra break");
for (let contando = 0; contando < 7; contando++) {
    if (contando % 2 === 0) {
        console.log("contando = " + contando);
        break; // En JavaScript no hay labels para break/continue
    }
}