'''
10. Un analista económico utiliza un programa que toma desde una tupla valores de la cotización en pesos
del dolar blue en los últimos 5 días:
dolarBlue = ( "189 "," 1930 "," 187 "," 210 "," 202 ")
con el propósito de utilizarlos en un determinado informe. El programador se ha dado cuenta que
necesita modificar la segunda posición del mismo, porque hay un error de entrada del dato. ¿Qué
solución propone para enmendar este problema?.
'''

dolarBlue = ("189","1930","187","210","202")

temp = dolarBlue[:1]+(193,)+dolarBlue[2:]
print(temp)
