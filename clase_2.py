'''Clase 2 de Programación 1
Agenda:
1. Operadores aritméticos
2. Tipos de datos
3. Asignación
4. Expresiones
'''


print("")   #### salto de linea para vizualizar mejor en consola
######################################################################
'''1. Operadores aritméticos

- suma: +
- resta: -
- multiplicación: *
- división: /
- exponencial: **
- floor division: //
- módulo: %

La jerarquia de los operadores aritméticos es la misma que conocemos de matemáticas.

Las jerarquía de menor a mayor, siendo la menor la dominante.

Valor Jerárquico    Operador                Nombres

      0                ()                 paréntesis
      1              % , **            Módulo, potencia
      2            * , /, //     producto, división, floor division
      3               + , -                suma, resta

'''

print('####### Operadores aritméticos #######')
print("")   #### salto de linea para vizualizar mejor en consola
a = 2
b = 6

print('Prueba de suma: ', a + b)
print('Prueba de resta: ', a - b)
print('Prueba de multiplacación: ', a * b)
print('Prueba de división: ', a / b)
print('Prueba de exponencial: ', a ** b)
print('Prueba de floor división: ', b // a)
print('Prueba de módulo: ', b % 2)

## Resolver


print("")   #### salto de linea para vizualizar mejor en consola
print("")   #### salto de linea para vizualizar mejor en consola

######################################################################
'''2. Tipos de datos
A continuación definimos una lista con sus nombres en español/inglés/ y el nombre asignado dentro de Python (tipo).

Todos los programas trabajan con objetos de datos. Dentro de este conjunto diferenciamos 2
subconjuntos

Escalar (Un dato atómico y unidimensional.)
- Enteros/Integers: int
- Flotantes/Floats: float
- Booleano: bool
- NoneType: None    Solo mencionar por ahora.

No Escalar (tiene una estructura interna a la que se puede acceder)
- Cadena/String: str
-
-
'''


print('####### Tipos de datos #######')
print("")   #### salto de linea para vizualizar mejor en consola
entero = 3      # números enteros
flotante = 3.0  # números reales
cadena = '3'


#Cuando los imprimimos se ven bastante parecidos
print(entero, '/', flotante, '/', cadena)

#Y python nos ayuda a ver el tipo de dato
print(type(entero), type(flotante), type(cadena))

#Pero no siempre podemos operar con ellos
print(entero + flotante)

# print(entero + cadena) #descomentar para ver error
print(entero * cadena)

# print(flotante * cadena) #descomentar para ver error
print(True)
print(False)

print("")   #### salto de linea para vizualizar mejor en consola
#Tambien podemos pasar de un tipo a otro:
print(type(entero))

print(type(str(entero))) #pasar el entero a cadena

print(entero + int(cadena)) #pasar la cadena a entero

flotante2 = 3.7
print(flotante2)
print(int(flotante2))  # corta la parte decimal.


# INT y FLOAT  y los
queTipo1 = entero * flotante
queTipo2 = entero / flotante
queTipo3 = entero // flotante
queTipo4 = entero // entero

##type(queTipo1)

type(True)
print(int(True))
print(int(False))


print("")   #### salto de linea para vizualizar mejor en consola
print("")   #### salto de linea para vizualizar mejor en consola
######################################################################
'''3. Asignación
Le asignamos un valor a una variable.'''


print('####### Asignación #######')
print("")   #### salto de linea para vizualizar mejor en consola

var1 = 2
var2 = 3

print(var1 + var2)



######################################################################

'''4. Expresiones
Una combinación de valores, variables y operadores'''
#para evaluar en la consola
print('####### Expresiones #######')

42
var1 + var2

'''Ejercicio
Generará un código que permita calcular el área de un círculo. El código debe ser reutilizable
# Ayuda 1 : Utilizando la funcion input("**************") se puede ASIGNAR a una variable un #valor que el usuario ingresa por consola. Para luego ser usado llamando la variable.
# Ayuda 2 : La función input devuelve una cadena ¿que tipo de datos necesitamos? Como lo modifico para utilizarlo en nuestro ejemplo?
'''





print("")   #### salto de linea para vizualizar mejor en consola
print("")   #### salto de linea para vizualizar mejor en consola
######################################################################
'''5. Operaciones con cadenas:

- Concatenación: +
- Repetición: *'''
print('####### Operaciones con cadenas #######')
print("")   #### salto de linea para vizualizar mejor en consola


# facultad = 'FCEIA'
# print('La ' + facultad + ' es parte de la UNR')

# repetir = 3
# print(repetir * facultad)






'''Ejemplo de uso para la asignacion, concatenación y la repetición: La intensidad del gol.
Utilicemos el partido que juega la seleccion Argentina y  la Ecuatoriana a las 20.30 hs por eliminatorias para construir un ejemplo.
Imaginemos que podemos extender la pronunciacion de la palabra gol en el relato del partido de hoy contra Ecuador por medio de pyhton. En relacion a la calidad del gol y a la parcialidad del relator Argentino.
'''
inten = int(input(" 2 si es de Ecuador y 30 si es de Argentina:   "))


# ASIGNAMOS el gol.
gol = "G"+inten*"0"+"L!"

# ASIGNAMOS los complementos del relato según selección.
Ecuador = " de la selección Ecuatoriana"
Argentina = " de la Scaloneta que defiende su invicto de 30 partidos"

# Utilicemos, entonces, las variable adecuadas para constriur el relato.
relato = (gol + Argentina)
print(relato)


print("")   #### salto de linea para vizualizar mejor en consola
print("")   #### salto de linea para vizualizar mejor en consola







'''Ejercicio
Generar un programa que le pregunte a la persona su nombre y que genere un saludo acorde
Ayuda: utilizando la funcion input("**************") se puede ASIGNAR a una variable un #valor que el usuario ingresa por consola. Para luego ser usado llamando la variable.
'''


'''Bibliografía:
- Downey, A. 2016. "Think Python, How to think like a computer scientist". Publicado por O'Reilly '''
