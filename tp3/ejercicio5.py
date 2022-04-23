'''
4. Una marca de ropa tienen descuentos diferentes dependiendo de la sede del local:
Item
 Rosario
 Funes
 Roldán
Zapatillas
 30 %
 40 %
 25 %
Remeras
 20 %
 30 %
 15 %
Pantalones
 10 %
 5%
 20 %
Dado un item y la sede del local, devolver el descuento que se recibirá.

5. Ahora, supongamos que además dependiendo del día de la semana se puede recibir un descuento
adicional acumulable. Es decir, si se recibió un descuento del 10 % según el ítem y la sede y la compra
se realiza un lunes, el descuento total será un 20 % . Escribir un programa en el que la persona pueda
ingresar el día de la semana, el item a comprar y la sede del local. Luego, informar el descuento total
a recibir. Utilizar la siguiente tabla de descuentos
Lunes
 Miércoles
 Jueves
Descuento
 10 %
 8%
 5%


'''

#datos
dia = input("Ingrese el dia de la semana: ") 
item = input("Ingrese el item: ") 
sede = input("Ingrese la sede: ")

#procesamiento
dia = dia.lower() #paso todo a minuscula
item = item.lower() #paso todo a minuscula
sede = sede.lower() #paso todo a minuscula

descuento = 0 
if item == 'zapatillas':
    if sede == 'rosario':
        descuento = 30
    elif sede == 'funes':
        descuento = 40
    elif sede == 'roldán':
        descuento =  25
    else:
        descuento = 0
elif item == 'remeras':
    if sede == 'rosario':
        descuento = 20
    elif sede == 'funes':
        descuento = 30
    elif sede == 'roldán':
        descuento =  15
    else:
        descuento = 0    
elif item == 'pantalones':   
    if sede == 'rosario':
        descuento = 10
    elif sede == 'funes':
        descuento = 5
    elif sede == 'roldán':
        descuento =  20
    else:
        descuento = 0    
else: 
    print("El item ingresado no es válido.")

if dia == 'lunes':
    descuento = descuento + 10
elif dia == 'miércoles':
    descuento = descuento + 8
elif dia == 'jueves':
    descuento = descuento + 5
    
#salida
if (descuento > 0):
    print("Descuento a pagar: ", descuento,"%")
else:
    print("Sin descuento.")