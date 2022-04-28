'''
4.7 Dado 10 n´umeros, informar el rango de los mismos [menor, mayor]. 
Codificar en lenguaje Python y ejecutar el programa. Verificar los resultados.
4.8 Se ingresan 10 n´umeros. Determinar el Promedio de los mismos.
'''

from re import X


minimo = None #ToDo: Esta bien esto?
maximo = None
promedio = 0

for i in range(10):
    x = int(input("Ingrese un entero: "))
    if (minimo is None):
        maximo = x
        minimo = x
    elif (x>maximo):
        maximo = x
    elif (x<minimo):
        minimo = x
    promedio += x #Sumo todos los numeros ingresados

promedio /= 10 #Divido por la cantidad de numeros ingresados

print("Minimo: ", minimo)
print("Maximo: ", maximo)
print("Promedio: ", promedio)

