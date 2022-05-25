'''
8. Escribir un programa que dada una fecha expresada como la terna (Día, Mes, Año) 
(donde Día, Mes y Año son números enteros) calcule el día siguiente al dado, en el mismo formato.
'''

fecha=(31,12,2022)
dia, mes , año = fecha
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

fecha_siguiente = (dia, mes, año)
print(fecha_siguiente)