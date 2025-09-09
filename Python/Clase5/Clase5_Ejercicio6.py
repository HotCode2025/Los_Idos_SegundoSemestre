#Calculadora de impuesto: 
#Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado(IVA).
#Formula:pago_total= pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
#Proporcione el pago sin impuesto:1000
#Proporcione el monto total del impuesto: 21%
#Pago con impuesto: xxxx

def calcular_pago_con_impuesto(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total

pago_sin_impuesto = 1000
impuesto = 21

# Llamamos a la función
pago_con_impuesto = calcular_pago_con_impuesto(pago_sin_impuesto, impuesto)

# Mostramos el resultado de la calculadora de impuesto
print("Pago con impuesto: ", pago_con_impuesto)
print("Pago sin impuesto: ", pago_sin_impuesto)