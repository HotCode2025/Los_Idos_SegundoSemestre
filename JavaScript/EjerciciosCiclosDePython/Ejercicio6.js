// Ejercicio 6 - Palabra reservada Continue
// Primera forma
for (let i = 0; i < 6; i++) {
    if (i % 2 === 0) {
        console.log(`valor: ${i}`);
    }
}

// Segunda forma con continue
for (let i = 0; i < 6; i++) {
    if (i % 2 !== 0) {
        continue;
    }
    console.log(`valor: ${i}`);
}