'''
El objetivo de este ejercicio es recolectar datos de personas y almacenarlos en una especie de base de
datos. A través de lo diferentes ítems, los iremos guiando en la creación de la misma.
a. Escribir un programa que le pida al usuario ingresar por consola los siguientes datos por separado:
Nombre, Apellido, Localidad, Edad, DNI, Carrera universitaria en curso, año de inicio de la
carrera. Guardar los datos en una lista llamada datos_personales e imprimirlos en pantalla.
'''
'''
b. A partir de la lista del ejercicio anterior, genere un programa que calcule los años que la persona
lleva cursando la carrera y lo agregue a la lista. Por ejemplo, si la persona inició su carrera en el
2019, la cantidad de años cursados a agregar es 4.
'''
'''
c. Utilice el código de los ítems de arriba y automatice la recolección de datos para una cantidad de
personas desconocidas. El resultado de este ejercicio debe ser una lista llamada basedatos donde
se almacenarán las listas datos_personales de cada individuo que se recolecten
'''
'''
d. Realice un programa que modifique para cada persona la carrera en curso por la palabra "TUIA"
'''

campos_personales = ['Nombre', 'Apellido', 'Edad', 'Carrera','Año de Inicio']
basedatos = []

respuesta = "si"
while respuesta.lower() =="si":
    datos_personales = []
    for x in campos_personales:
        valor = input("Ingrese su "+ x+ ": ")
        datos_personales.append(valor)
        if x == 'Año de Inicio':
            años = 2022 - int(valor)
            datos_personales.append(años)
    #Finalmente, imprima una frase que indique el nombre, el apellido y cantidad de años cursados de la persona
    print("El alumno: ", datos_personales[0], datos_personales[1], " lleva ", datos_personales[-1], " años de cursado" )
    basedatos.append(datos_personales)
    respuesta = input("Desea cargar otra persona? (SI/NO): ")
    #print(datos_personales)

print(basedatos)

basedatos2 = []
for persona in basedatos:
    persona[-3] = "TUIA"
    basedatos2.append(persona)

print(basedatos2)
