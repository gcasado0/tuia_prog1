"""
Dado el siguiente diccionario:
"""

feriados = {'año nuevo' : (1, 1, 2022),
            'carnavales' : [(26,2,2022),(27,2,2022),(28,2,2022), (1,3,2022)],
            'dia de la memoria' : (24,3,2022),
            'Malvinas' : (2,4,2022),
            'semana santa' : [(14,4,2022), (15,4,2022), (16,4,2022),(17,4,2022)],
            'dia del trabajador' : (1,5,2022),
            'Censo nacional 2022': (18,5,2022),
            'Revolucion de mayo' : (25,5,2022),
            'Guemes': [(17,6,2022),(18,6,2022),(19,6,2022)],
            'Belgrano': (20,6,2022),
            'Independencia': (9,7,2022),
            'San Martin': (15,8,2022),
            'Feriado con fines turísticos': (7,10,2022),
            'Día del Respeto a la Diversidad Cultural': (10,10,2022),
            'Día de la Soberanía Nacional': (20,11,2022),
            'Inmaculada Concepción de María': (8,12,2022),
            'Feriado con fines turísticos': (9,12,2022),
            'Navidad': (25,12,2022)
      }

"""
1. Agregar los feriados restantes, si son feriados largos, agregarlos como una lista de tuplas.
2. Hay un feriado largo en el mes de Junio, actualizar el diccionario para que quede acorde al formato. (Contar como feriados los fines de semana de ser necesario)
3. Pedirle al usuario que ingrese un feriado, si se encuentra en el diccionario informarle cuantos días tiene, caso contrario pedirle que lo ingrese nuevamente.
4. Crear un diccionario sólo con los feriados de un sólo día.
5. Informar cuantos feriados largos hay en el año y crear una lista con los nombres.

*Nota:* La funcion  isinstance(object, classinfo) devuelve si un objeto es una instancia de una clase o de una subclase de la misma. Por ejemplo:


"""
var = 'a'
print( isinstance(var, int) )  # False
print( isinstance(var, str) )  # True



#3. Pedirle al usuario que ingrese un feriado, si se encuentra en el diccionario informarle cuantos días tiene, caso contrario pedirle que lo ingrese nuevamente.

nombre = input("Ingrese un feriado: ")
while nombre:
      if nombre in feriados:
            if isinstance(feriados[nombre],tuple):
                  print("El feriado tiene 1 dia")
            else:
                  print("El feriado tiene ",len(feriados[nombre])," dias")
            break
      else:
            print("El feriado no existe.")
            nombre = input("Ingrese un feriado: ")



#4. Crear un diccionario sólo con los feriados de un sólo día.

feriados_unitarios = {}
for clave, valor in feriados.items():
      if isinstance(valor,tuple):
            feriados_unitarios[clave]=valor
print("feriados_unitarios =", feriados_unitarios)

#5. Informar cuantos feriados largos hay en el año y crear una lista con los nombres.
feriados_largos = []
for clave, valor in feriados.items():
      if isinstance(valor,list):
            feriados_largos.append(clave)
print("feriados_largos =", feriados_largos)