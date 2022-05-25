'''
14.Escribir un programa que recibe un diccionario que tiene como llave a alumnos y los valores asociados
una lista con las notas de parciales de los alumnos. El programa debe calcular el promedio de cada
alumno e imprimirlo en pantalla. Por ejemplo para
alumnos = {" Juan ": [6 ,9 ,8] , " Manuel ": [9 ,10 ,9] , " Martin ": [5 ,6 ,7]}
'''

alumnos = {"Juan":[6,9,8],"Manuel":[9,10,9],"Martin":[5,6,7]}

for alumno, notas in alumnos.items():
    suma = 0
    cantidad = 0
    for x in notas:
        suma += x
        cantidad += 1
    promedio = suma/cantidad
    print(alumno, promedio)