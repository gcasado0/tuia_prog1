'''
13. Escribir un programa que toma una lista de tuplas con el formato (Alumno, Nota) donde alumno es
una cadena con el nombre del alumno y nota es un número.
Ejemplo: [('Perez', 8), ('Gonzalez', 10), ('Fernandez', 10)]
a. Crear un diccionario donde las claves son los alumnos y el valor asociado una lista que contenga
las notas del alumno.
Ejemplo_dict = { 'Perez ': [8] , 'Gonzalez ': [10] , 'Fernandez ': [10]}
b. Crear un diccionario donde las claves son las notas y el valor asociado una lista que contenga los
alumnos que obtuvieron esa nota en un parcial
Ejemplo_dict2 = {8: [ 'Perez '] , 10: ['Gonzalez ', 'Fernandez ']}
'''

notas = [('Perez', 8), ('Gonzalez', 10), ('Fernandez', 10), ('Perez',7)]

dicc1 = {}
for alumno, nota in notas:
    if alumno in dicc1:
        dicc1[alumno].append(nota)
    else:        
        dicc1[alumno] = [nota]

print(dicc1)

dicc2 = {}
for alumno, nota in notas:
    if nota in dicc2:
        dicc2[nota].append(alumno)
    else:        
        dicc2[nota] = [alumno]

print(dicc2)
