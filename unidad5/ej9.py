'''
9. Escribir un programa que dada una fecha expresada como la terna (Día, Mes, Año) 
(donde Día y Año son números enteros, y Mes es el texto "Ene", "Feb",. . ., "Dic", según corresponda) 
calcule el día siguiente al dado, en el mismo formato.
'''

meses = ("Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic")
fecha = (28,'Feb',2022)
dia, mes_alfa , año = fecha
mes = meses.index(mes_alfa) + 1

dia = dia +1
if mes in (1,3,5,7,8,10,12):
    if dia == 32:
        dia = 1
        mes += 1
elif mes == 2:
    if dia==29:
        dia = 1
        mes += 1
else:
    if dia==31:
        dia = 1
        mes += 1

if mes==13:
    mes = 1
    año +=1

mes_alfa = meses[mes-1]
fecha_siguiente = (dia, mes_alfa, año)
print(fecha_siguiente)