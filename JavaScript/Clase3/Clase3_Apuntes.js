//Hoisting: Podemos llamar la funcion en cualquier parte (Antes o despues de definirla)
miFuncion(8, 2);//Esto se conoce como hosting

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a + b));
    return a + b;
}

//Llamando la funcion
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado)

//Funciones de tipo expresion o anonima:
let x = function(a, b){return a + b;} //Necesita estar cerrado con punto y coma
resultado = x(5 ,6); //Al llamarla se pone la variable y paréntesis
console.log(resultado);

//Funciones de tipo Self y invoking
(function(a, b){
    console.log('Ejecutando la funcion: ' + (a+b));
})(9, 6);//Aca se llama asi misma con parametro, se manda a llamar esta funcion una única vez

//Tipo de dato de una función
console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
}
miFuncionDos(5, 7)

//toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

//Funciones flecha: No se usa la palabra function, no llaves, no return
const sumarFuncionFlecha = (a, b) => a +b; //Construimos la funcion flecha
resultado = sumarFuncionFlecha(3, 7); //Asignamos el valor a una variable
console.log(resultado)

//Argumentos: Cuando llamamos a la funcion, y colocamos valores.
//Parámetros: CUANDO DEFINIMOS UNA FUNCIÓN, DENTRO DE LOS PARENTESIS SE DEFINEN DOS VARIABLES 
//Funcion de tipo expresión
let sumar = function(a = 4, b = 8){
    console.log(arguments[0]);// muestra el parametro de A
    console.log(arguments[1]); //Muestra el parametro de B
    console.log(arguments[2]);
    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado)
//No es necesario que coincida el numero de arguntos con el numero de parametros


//Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9)
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for (let i = 0; i < arguments.length; i++){
        suma += arguments[i]; //Arguments es para arreglos
    }
    return suma;

}

//Tipos primitivos
//Paso por valor: Es cuando utilizamos tipos que no sonobjetos: numericos, booleanos
let k = 10;
function cambiarValor(a){ //Paso por valor: La variable inicializada no sufre ningun cambio
    a = 20;
}

cambiarValor(k);
console.log(k);

//Paso por referencia: al metodo le pasamos la referencia hexadecimal de el espacio de memoria donde se guarda el objeto 
const persona = {
    nombre:'Juan',
    apellido: 'Lepez'
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}

cambiarValorObjeto(persona);
console.log(persona);
