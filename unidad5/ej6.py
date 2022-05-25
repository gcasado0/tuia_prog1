'''
6. Cartas como tuplas.
a. Proponer una representación con tuplas para las cartas de la baraja francesa.
b. Escribir un programa de poker que reciba cinco cartas de la baraja francesa e informe (devuelva
el valor lógico correspondiente) si esas cartas forman o no un poker (es decir que hay 4 cartas con
el mismo número).
'''

#carta = ('corazones',1)
juego = []
numeros=[]

for i in range(5):
    palo = input("Ingrese el palo: (P,C,D,T): ")
    numero = input("Ingrese el numero: (1..13): ")
    carta = palo, numero
    juego.append(carta)
    numeros.append(numero)

print(juego)

for numero in numeros:
    if numeros.count(numero)==4:
        print("Es poker")
        break


