'''
2.2 Se ingresa un n´umero por teclado:
a. Informar si es positivo o negativo.
b. Informar si es par o impar.
'''

x = int(input("Ingresar un numero entero: "))

if (x>0):
    print("Es positivo")
if (x<0):
    print("Es negativo")

if (x%2==0):
    print("Es par")
else:
    print("Es impar")