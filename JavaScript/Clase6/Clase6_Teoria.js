//Clase6_JavaScript_Teoría

//Clases
//La clase es una plantilla, en la cual definimos los atributos/metodos que van a tener los objetos (instancias) que contenga.

//Sintáxis básica para crear una clase
class Persona{ //Clase Padre (Parent)
    constructor(nombre, apellido){      //Si no se define un constructor, JS crea uno de manera automática.
        this._nombre = nombre;
        this._apellido = apellido;  //Buena práctica: los atributos de la clase no pueden llamarse igual cuando las llamamos (get/set), por eso se usa un guion.

    };

    get nombre(){
        return this._nombre;
    };
    
    set nombre(nombre){
        return this._nombre = nombre;
    };

    get apellido(){
        return this._apellido;
    };

    set apellido(apellido){
        return this._apellido = apellido;
    };

}

//Herencia
class Empleado extends Persona{ //Clase Hija (Child) --> Ver Diagrama UML
    constructor (nombre, apellido, departamento){
        super(nombre, apellido) //Tenemos que llamar al constructor de la CLASE PADRE usando super() EN LA PRIMERA LÍNEA del constructor Child.
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }
}

let persona1 = new Persona('Martin', 'Perez');
//console.log(persona1);
console.log(persona1.nombre); //llamamos al atributo con el método get (está dentro de los paréntesis ".") (definido en la clase)
persona1.nombre = 'Juan Carlos'; //cambiamos el nombre usando el método set (definido en la clase)
console.log(persona1.nombre);
console.log(persona1.apellido); //Traemos el atributo actual del objeto (definido en lin 18)
persona1.apellido = 'Martinez'; //Modificamos el segundo atributo con el método get.
console.log(persona1); //Imprmimios el objeto con los nuevos atributos
let persona2 = new Persona('Carlos', 'Lara');
//console.log(persona2);
console.log(persona2.nombre);
persona2.nombre = 'María Laura';
console.log(persona2.apellido);
persona2.apellido = 'Castro';
console.log(persona2);

//Hoisting 
//NO funciona para clases, es decir, no puedo llamar una instancia de la clase antes de inicializarla/definirla.

//HERENCIA
//Creamos un objeto de la clase Child (Definida en línea 33)
let empleado1 = new Empleado('Nicolas', 'Giglio', 'QA');
console.log(empleado1);
console.log(empleado1._nombre) //El atributo "nombre" está HEREDADO de la clase PARENT (Persona).
