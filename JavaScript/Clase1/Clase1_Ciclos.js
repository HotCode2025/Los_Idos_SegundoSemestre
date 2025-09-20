//WHILE
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo While")


//DO WHILE: Primero se ejecuta todo el codigo y al último la condición
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("Fin del ciclo Do While");


//Ciclo FOR
for ( let contando = 0; contando < 3; contando++){
    console.log(contando);
}
console.log("Fin del ciclo For");


//Palabra reservada Break

for(let contando = 0; contando <= 10; contando++ ){
    if (contando % 2 == 0){
        console.log(contando) //mostramos todos los pares
        break;//Rompe cualquiera sea la estructura, al cumplir el ciclo.
    }
}

console.log("Termina el ciclo al encontrar el primer numero par pares");

//Palabra reservada continue y Etiquetas Labels

inicio:
for(let contando = 0; contando <= 10; contando++ ){
    if (contando % 2 !== 0){
        break inicio;// ir a la siguiente iteración
    } 
    console.log(contando)
}   
console.log("Termina el ciclo")


