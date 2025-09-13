//Clase5_JavaScript_Teoría

//Continuamos con los metodos get y set.
let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log("Tipos primitivos");

//Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 30,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase();  //método toUppercase convierte las minúsculas en mayúsculas.
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },    
    nombreCompleto: function(){ //Metodo o funcion en js
        return this.nombre+" "+this.apellido;
    },
    get nombreEdad(){
        return 'El nombre es: '+this.nombre+', edad: '+ this.edad;
    }

}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando como un objeto");

let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Salada 14";
persona2.telefono = "5492614269594";
console.log(persona2.telefono);
console.log("Creamos un nuevo objeto");
console.log(persona["apellido"]); //Accedemos como si fuera un arreglo
console.log("Usamos el ciclo for in");
//for in y accedemos al objeto como si fuera un arreglo
for (propiedad in persona){
    console.log(propiedad); 
    console.log(persona[propiedad]); //accede a lo que contiene la propiedad(su valor)
}

console.log("Cambiamos y eliminamos un error");
persona.apellida = "Betancud"; //Cambiamos dinamicamente un valor del objeto
delete persona.apellida; //Eliminamos el error 
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: concatenar cada valor de cada propiedad
console.log("Distintas formas de imprimir un objeto: forma 1");
console.log(persona.nombre+" "+persona.apellido);

//Numero 2: A traves del ciclo for in
console.log("Distintas formas de imprimir un objeto: forma 2");
for (nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Object.values()
console.log("Distintas formas de imprimir un objeto: forma 3");
let personaArray = Object.values(persona);
console.log(personaArray);


//Numero 4: Utilizaremos el metodo JSON.stringify
console.log("Distintas formas de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

//Acá utilizamos el método get (línea 15)
console.log('Comenzamos a utilizar el método get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el método get para idiomas');
console.log(persona.lang);

//Llamamos el método set (línea 18)
persona.lang = 'en';
console.log(persona.lang);

//CONSTRUCTORES DE OBJETOS

function Persona3(nombre, apellido, email){  //Constructor: Nos permite crear varios objetos con la misma estructura a diferencia de la clase.
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Roberto', 'Gomez','rgomez@gmail.com');
padre.nombre = 'Luis'; //Cada modificación afecta al objeto en cuestión y no a los demás.
console.log(padre);
console.log(padre.nombreCompleto()) //Utilizamos el método asignado al objeto (línea 96)
padre.telefono = '2634556677'; //Puedo agregar una propiedad y pertenece únicamente a este objeto
console.log(padre);

let madre = new Persona3('Laura', 'Contreras','lcontreras@gmail.com');
console.log(madre);
console.log(madre.nombreCompleto());
console.log(madre.telefono) // En este caso la propiedad no está definida como en el objeto padre (línea 104).
// Distintas formas de crear objetos

//caso objeto 1
let miObjeto = new Object(); //Esta es una opción formal.
//caso objeto 2
let miObjeto2 = {}; //Esta opción es breve y recomendada.

//caso String 1
let miCadena1 = new String('Hola'); //Sintaxis formal.
//caso String 2
let miCadena2 = 'Hola'; //Esta es la sintáxis simplificada y recomendada.

//caso con números 1
let miNumero = new Number(1); //Es formal no recomendable.
//caso con números 2
let miNumero2 = 2; //Sintáxis recomendada.

//caso boolean 1
let miBoolean1 = new Boolean(false); //Formal.
//caso boolean 2
let miBoolean2 = false; //Sintaxis recomendada.

//caso Arreglos 1
let miArreglo1 = new Array(); //Formal.
//caso Arreglos 2
let miArreglo2 = []; //Sintaxis recomendada.

//caso function 1
let miFuncion1 = new function(){};  //Todo después de "new" es considerado objeto.
//caso function 2
let miFuncion2 = function(){}; //Notación simplificada y recomendada.

//Uso de prototype: Permite agregar propiedades para TODOS los objetos que quiero.
Persona3.prototype.telefono = '26123232311'; //Con el comando 'prototype' se agrega la propiedad a todos los objetos tipo "Persona3"
console.log(padre)
console.log(madre.telefono);
madre.telefono = '45623444123';
console.log(madre.telefono);


//Uso de call: permite llamar y asignar un método asignado a OTRO objeto previamente.
let persona4 = {
    nombre: 'Juan',
    apellido:  'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}
console.log(persona4.nombreCompleto2('Lic.', '2311233124'))
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '7862366123'));

//Uso de apply: similar al método call, es una llamada al método de otro objeto.
let arreglo = ['Ing.', '1233311313'] //Este arreglo es lo que le vamos a pasar al método apply.
console.log(persona4.nombreCompleto2.apply(persona5, arreglo)); //La diferencia con el método call es cómo se pasan los argumentos a los métodos.
//Usando apply se tiene que pasar los argumentos con un arreglo.