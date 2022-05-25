'''
16. Dadas dos listas donde la primera contiene nombres de personas y la segunda sus edades, generar un
diccionario a partir de ellas. Investigar cómo la función zip() puede ayudar en la resolución
'''

nombres = ['gustavo','carolina','pedro','luciano']
edades = [49,41, 21, 23]

lista = list(zip(nombres,edades))
dicc = dict(lista)
print(lista)
print(dicc)