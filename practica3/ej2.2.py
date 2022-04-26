'''
2.2 Dado dos numeros enteros N y M, informar si N es multiplo de M. Codificar en lenguaje Python y
ejecutar el programa. Verificar los resultados.
'''

n = int(input("Ingresar un entero N: "))
m = int(input("Ingresar un entero M: "))

if (n>0 and m%n==0):
    print("N es multiplo de M")
else:
    print("N no es multiplo de M")

