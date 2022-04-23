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

'''

#datos
item = input("Ingrese el item: ") 
sede = input("Ingrese la sede: ")

#procesamiento
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

#salida
if (descuento > 0):
    print("Descuento a pagar: ", descuento,"%")
else:
    print("Sin descuento.")