'''
Calcule los n primeros números de la secuencia de Fibonacci en una lista. Es decir, el programa
comenzara con la lista [0,1] y computará iterativamente el siguiente número de la secuencia.
'''

n=100
lista_fb = [0, 1]

for i in range(2,n):
    numero = lista_fb[i-1] + lista_fb[i-2]
    lista_fb.append(numero)

print(lista_fb)