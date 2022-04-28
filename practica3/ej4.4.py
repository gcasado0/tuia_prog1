'''
4.4 Pedir 10 numeros y mostrar la suma de los pares y de los impares por separado. Verificar los resultados
utilizando la calculadora.
'''
pares = 0
impares = 0

for i in range(10):
    x = int(input("Ingrese un entero: "))
    if (x%2==0):
        pares += x
    else:
        impares +=x

print("Pares = ", pares)        
print("Impares = ", impares)        