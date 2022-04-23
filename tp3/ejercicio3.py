'''
3. En el centro de la ciudad de Rosario el estacionamiento en vía se encuentra tarifado y está dividido
en tres zonas con tarifas diferenciadas. El vehículo puede estacionarse como máximo por 3 horas en
el mismo sitio, luego de este tiempo, para renovar el servicio, hay que mover el vehículo. La siguinte
tabla muestra los costos por hora en cada una de las zonas:
Zona
 Primer hora
 Segunda hora
 Tercer Hora
A
 $57,00
 $71,20
 $85,50
B
 $47,00
 $58,70
 $70,50
C
 $37,00
 $46,20
 $55,50
Escribir un programa que dada la zona, A, B o C, y la cantidad de horas que el vehículo estará
estacionado, devuelva el costo a pagar. En caso de que el tiempo de estacionamiento supere las 3 horas,
imprimir un mensaje de error acorde.
'''

#datos
zona = input("Ingresa la zona: ") 
tiempo = float(input("Ingrese la cantidad de horas que el vehiculo estará estacionado: "))

#procesamiento
if tiempo > 3.0:
    print("El tiempo de estacionamiento ingresado no debe ser superior a las 3 horas.")
if tiempo < 0.0:
    print("El tiempo de estacionamiento ingresado no debe ser negativo.")

costo = 0 
if zona == 'A' or zona == 'a':
    if tiempo <= 1.0:
        costo = 57.00
    elif tiempo <= 2.0:
        costo = 71.20
    else:
        costo =  85.50
elif zona == 'B' or zona == 'b':
    if tiempo <= 1.0:
        costo = 47.00
    elif tiempo <= 2.0:
        costo = 58.70
    else:
        costo =  70.50
elif zona == 'C' or zona == 'c':    
    if tiempo <= 1.0:
        costo = 37.00
    elif tiempo <= 2.0:
        costo = 46.20
    else:
        costo =  55.50
else: 
    print("La zona ingresada no es válida.")

#salida
if (costo > 0):
    print("Costo a pagar: ", costo)