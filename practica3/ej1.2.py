'''
1.2 Pedir el valor de 3 variables, realizar y mostrar el resultado de:
a. La suma de las dos primeras
b. El producto de las dos ´ultimas
c. Reemplazar el valor de la 3ra. por el triple de la primera
'''

#entrada
x = float(input("Ingresar x: "))
y = float(input("Ingresar y: "))
z = float(input("Ingresar z: "))

#procesamiento
suma = x + y
producto = y * z
z = 3 * x

#salida
print("La suma de las dos primeras:", suma)
print("El producto de las dos ultimas: ", producto)
print("El valor de la 3ra. por el triple de la primera: ", z)


