'''
4.4 Dadas las notas de los 85 estudiantes que rindieron un examen, informar el porcentaje de notas superiores
a 7.
'''

notas_mayor_7=0
n = 10 # 85 cantidad de estudiantes

for i in range(1,n+1):
    nota = int(input("Ingrese resultado de examen #"+str(i)+": "))
    if (nota>7):
        notas_mayor_7 +=1


print("Porcentaje de notas superioresa 7:" ,notas_mayor_7*100/n, "%")