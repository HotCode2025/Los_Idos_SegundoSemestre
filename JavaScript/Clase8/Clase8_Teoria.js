//Clase8_JavaScript_Teoría

//Clases
//La clase es una plantilla, en la cual definimos los atributos/metodos que van a tener los objetos (instancias) que contenga.

//Sintáxis básica para crear una clase
class Persona{ //Clase Padre (Parent)
    
    static contadorPersonas = 5; //Atributo estático
    // email = 'Valor default email' //Atributo no estático
    static get MAX_OBJ(){ //Este método simula una constante.
        return 5;
    }
    
    constructor(nombre, apellido){      //Si no se define un constructor, JS crea uno de manera automática.
        this._nombre = nombre;
        this._apellido = apellido;  //Buena práctica: los atributos de la clase no pueden llamarse igual cuando las llamamos (get/set), por eso se usa un guion.
        Persona.contadorPersonas++;
        this.idPersona = ++Persona.contadorPersonas;
        //console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
        if(Persona.contadorPersonas < Persona.MAX_OBJ){

            this.idPersona = ++Persona.contadorPersonas;
        }
        else{
            console.log("Se ha superado el máx de objetos definidos")
        }
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

    nombreCompleto(){
        return this.idPersona+' '+this._nombre+' '+this._apellido;
    }

    toString(){ //Regresa un String
        return this.nombreCompleto();
    }

    static saludar(){
        console.log('Saludos desde este método static');
    }

    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
    }

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

    //Sobreescritura del método nombreCompleto de la clase padre(linea 30)
    nombreCompleto(){
        //Se aplica el polimorfismo que sifnifica = múltiples formas en tiempo de ejecución
        //El método que se ejecuta depende si es una referencia de tipo padre o hija.
        return super.nombreCompleto()+', '+this._departamento;
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

//Herencia de Métodos (cont. Clase6)
console.log(empleado1.nombreCompleto()); //Vemos que la clase hija hereda el método nombreCompleto() (linea 30)

//Object.prototype.toString: Esta es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString()); //El método que se ejecuta, depende de la instancia de la clase (en este caso pertenece a la clase hija). Polimorfismo: posibilidad de llamar a métodos de clases padres/hijas según necesite.
console.log(persona1.toString());

//Llamamos al método static (lin 38)
//persona1.saludar(); el método static no se puede llamar desde el objeto, sólo dede la clase.
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//Referenciando un atributo tipo static
//console.log(persona1.contadorObjetosPersona); => Error porque se está referenciando desde el objeto y necesitamos hacerlo desde la clase.
console.log(Persona.contadorObjetosPersona); //Llamamos a los atributos estáticos desde la clase padre (Persona)
console.log(Empleado.contadorObjetosPersona); //También podemos llamar desde la clase Child.

//Atributos no estáticos => Se asocian a OBJETOS
console.log(persona1.email);
console.log(empleado1.emial);
//console.log(Persona.email) => Como el atributo NO es estático, no se lo puede referenciar desde la clase.
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);
let persona3 = new Persona('Carla', 'Pertosi');
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10: No se puede modificar ni alterar.

let persona4 = new Persona ('Franco', 'Diaz')
console.log(persona4.toString());

let persona5 = new Persona('Liliana', 'Paz')
console.log(persona5.toString);