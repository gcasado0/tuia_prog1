'''
19. Cada profe de programación 1 tiene un diccionario donde guarda el legajo de cada alumne en la clave
y una lista con las notas de cada persona en el valor. Al cerrar el cuatrimestre, necesitan pasarle a
alumnado un solo diccionario con estos datos, generarlo. Revisar el método .update() para ver como
puede ayudarte a resolver el problema. Los diccionarios de cada comisión se ven así
com1 = {'legajo_11 ': [6 , 7 , 8] ,... , 'legajo_1m ': [3 , 8 , 9]}
com2 = {'legajo_21 ': [6 , 7 , 8] ,... , 'legajo_2n ': [3 , 8 , 9]}
com3 = {'legajo_31 ': [6 , 7 , 8] ,... , 'legajo_3j ': [3 , 8 , 9]}
com4 = {'legajo_41 ': [6 , 7 , 8] ,... , 'legajo_4k ': [3 , 8 , 9]}
El diccionario final debería verse así:
prog_1 = {'legajo_11 ': [6 , 7 , 8] ,... , 'legajo_1m ': [3 , 8 , 9] ,
'legajo_21 ': [6 , 7 , 8] ,.. , 'legajo_2n ': [3 , 8 , 9] ,
'legajo_31 ': [6 , 7 , 8]... , 'legajo_3j ': [3 , 8 , 9] ,
'legajo_41 ': [6 , 7 , 8] ,... , 'legajo_4k ': [3 , 8 , 9]}
'''

com1 = {'legajo_11': [6 , 7 , 8] , 'legajo_1m': [3 , 8 , 9]}
com2 = {'legajo_21': [6 , 7 , 8] , 'legajo_2n': [3 , 8 , 9]}
com3 = {'legajo_31': [6 , 7 , 8] , 'legajo_3j': [3 , 8 , 9]}
com4 = {'legajo_41': [6 , 7 , 8] , 'legajo_4k': [3 , 8 , 9]}

prog_1 = {}
prog_1.update(com1)
prog_1.update(com2)
prog_1.update(com3)
prog_1.update(com4)

print(prog_1)

