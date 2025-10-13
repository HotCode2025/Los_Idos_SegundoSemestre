class Cliente extends Persona{
    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }

    get idcliente(){
        return this._idCliente;
    }

    get fechaRegsitro(){
        return this._fechaRegistro;
    }

    set fechaRegistro(fechaRegistro){
        this._fechaRegistro = fechaRegistro;
    }

    toString(){
        return ` 
        ${super.toString()}
        ${this._idCliente}
        ${this._fechaRegistro}`;
    }
}