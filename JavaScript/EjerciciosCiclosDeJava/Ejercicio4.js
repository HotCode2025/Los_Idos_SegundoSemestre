// Ejercicio 4 - Ciclo For con Continue
console.log("\nCiclo For, números pares Continue");
for (let contando = 0; contando < 7; contando++) {
    if (contando % 2 !== 0) {
        continue;
    }
    console.log("contando = " + contando);
}