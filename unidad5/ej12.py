'''
12. Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de
cada palabra en la cadena.
'''

cadena = "la peluca de la abuela es gris y de pelo de verdad"

palabra = ""
palabras = []
for x in cadena:
    if x == ' ':
        palabras.append(palabra)
        palabra = ""
    else:
        palabra += x
if palabra != "":
    palabras.append(palabra)

print(palabras)
dicc = {}
for x in palabras:
    if x in dicc:
        dicc[x] += 1
    else:
        dicc[x] = 1
print(dicc)