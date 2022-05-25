'''
7. El tiempo como tuplas.
a. Proponer una representación con tuplas para representar el tiempo.
b. Escribir un programa que reciba dos tiempos dados y devuelva su suma.
'''

#tiempo = (horas, minutos:0-59, segundos:0-59)

tiempo1 = (10,20,59)
tiempo2 = (11,40,59)

#suma = ( 22,1,58)

segundos = tiempo1[2]+tiempo2[2]
if (segundos>59):
    segundos=segundos-60
    minutos = 1
else:
    minutos = 0

minutos = minutos + tiempo1[1]+ tiempo2[1]
if (minutos>59):
    minutos=minutos-60
    horas = 1
else:
    horas = 0
horas = horas  + tiempo1[0]+ tiempo2[0]

tiempo3 = (horas, minutos, segundos)
print(tiempo3)