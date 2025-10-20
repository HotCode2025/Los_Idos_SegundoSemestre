
package domain;

public class Empleado extends Persona{
    //Atributos
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados;
    
    //Constructores
    public Empleado(){ //Constructor 1
        this.idEmpleado = ++contadorEmpleados;
    };
    
    public Empleado (String nombre , double sueldo){ //Constructor 2
        //super(nombre); => Usamos SUPER o THIS para llamar a un construcor interno. NO AMBOS.
        this(); //Estamos llamando desde aquí al constructor VACIO (llamar a un constructor interno. No se usan en conjunto con SUPER)
        this.nombre = nombre; //Acá accedemos al atributo de la clase padre (porque es de clase protected).
        this.sueldo = sueldo;
    }
    
    //Métodos
    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public void setIdEmpleado(int idEmpleado) {
        this.idEmpleado = idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
         sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
}   
