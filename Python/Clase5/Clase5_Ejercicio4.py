def multiplicar(*args):
    """Multiplica todos los valores numéricos recibidos."""
    resultado = 1
    for valor in args:
        if isinstance(valor, (int, float)):
            resultado *= valor
        else:
            raise ValueError(f"El valor '{valor}' no es numérico.")
    return resultado