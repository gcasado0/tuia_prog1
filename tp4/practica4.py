'''
variables de entrada:
dia del mes
tipo de empaque: 0 fin de carga, 1 unitario, 2 caja de 6 unidades
sabor: C-chocolate, D-dulce de leche, P-pasta de mani, M-mezcla
cantidad

El kiosco necesita saber:
- Para cada día del mes, los porcentajes de ventas de cada uno de los 3 sabores.
- La recaudación total del mes, sabiendo que cada cubanito cuesta $10.
- El día de mayor recaudación, informando también la recaudación correspondiente.
'''

recaudacion_mes = 0
maximo_dia = 0
maximo_recaudacion = 0
for dia in range(1,3): #24 dias habiles
    print("Dia ", dia)
    unidades_dia = 0
    unidades_C = 0
    unidades_D = 0
    unidades_P = 0
    unidades_M = 0
    
    tipo_empaque = int(input("Ingresar tipo empaque (1,2 o 0 para finalizar): "))
    while (tipo_empaque==1 or tipo_empaque==2):
        sabor = input("Ingrese el sabor (C-D-P-M): ")
        sabor = sabor.lower()
        cantidad = int(input("Ingrese la cantidad: "))
        if (tipo_empaque==1):
            unidades=1
        else:    
            unidades=6
        
        if sabor=="c":
            unidades_C += unidades * cantidad
        elif sabor=="d":
            unidades_D += unidades * cantidad
        elif sabor=="p":
            unidades_P += unidades * cantidad
        elif (unidades==6 and sabor=="m"):
            unidades_C += 2 * cantidad
            unidades_D += 2 * cantidad
            unidades_P += 2 * cantidad
        else:
            print("Error en el ingreso de sabor, reintente.")
        
        tipo_empaque = int(input("Ingresar tipo empaque: "))
    
    unidades_dia = unidades_C + unidades_D + unidades_P
    if (unidades_dia):
        porcentaje_C = unidades_C * 100/ unidades_dia
        porcentaje_D = unidades_D * 100/ unidades_dia
        porcentaje_P = unidades_P * 100/ unidades_dia
        print("Distribucion por sabor - Chocolate: %", round(porcentaje_C,2), " - Dulce de leche: %", round(porcentaje_D,2), " - Pasta de mani: %", round(porcentaje_P,2))
    
    recaudacion_dia = unidades_dia * 10 # costo cubanito $10
    if recaudacion_dia>maximo_recaudacion:
        maximo_recaudacion = recaudacion_dia
        maximo_dia = dia
    recaudacion_mes += recaudacion_dia

print("Dia de mayor recaudacion: ", maximo_dia, " con una recaudacion de: $", maximo_recaudacion)
print("Recaudación total del mes: $", recaudacion_mes)