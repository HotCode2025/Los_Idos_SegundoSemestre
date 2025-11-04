// Ejercicio 8 - Cálculo de salarios
let empleados = [
    { horas: 40, tarifa: 15 },
    { horas: 35, tarifa: 20 },
    { horas: 45, tarifa: 18 },
    { horas: 30, tarifa: 25 },
    { horas: 38, tarifa: 22 }
];

let suma_salarios = 0;

for (let i = 0; i < empleados.length; i++) {
    let salario = empleados[i].horas * empleados[i].tarifa;
    console.log(`El salario del empleado n.${i + 1} es $${salario}`);
    suma_salarios += salario;
}

console.log(`La sumatoria de todos los salarios es de $${suma_salarios}`);