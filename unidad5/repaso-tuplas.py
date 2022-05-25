tupla = ("abc", True, (1, 2), ['a', 'b'])
print(tupla)

print("index", tupla.index(True))
print("index", tupla.index((1, 2)))

tupla = tuple("1234")
print(tupla)

tupla = (10,)
print(tupla, type(tupla))

tupla1 = tuple(range(0, 15, 3))
print(tupla1, type(tupla))


tupla = (1, 2, 1, 1, 6, 'a', 'a')
print(tupla.count(1))  # 3

print(tupla.count('a'))  # 2

print(tupla.count([]))  # 0

print("Metodo 1")
for x in tupla:
    print(x)
print("Metodo 2")
for i in range(len(tupla)):
    print(tupla[i])
print("Metodo 3")
for i, x in enumerate(tupla):
    print(i, x)


tupla3 = tupla + tupla1
print(tupla3, len(tupla3))


alumnos = [("Martín", "Fernandez", "341556690", "mf10@gmail.com"),
("Juan Manuel", "Lopez", "113451098", "jml1999@gmail.com"),
("Pedro", "Casado", "341117788", "pc@hotmail.com"),
("Gustavo", "Casado", "341117789", "gcasado0rosario.gov.ar"),
("Gustavo", "Gonzalez", "342117789", "gz0rosario.gov.ar")]

 #¿Cuántos alumnos se llaman igual?
nombres = []
cantidad = 0
for nombre, apellido, telefono, email in alumnos:
    nombres.append(nombre)
for nombre in nombres:
    if nombres.count(nombre)>1:
        print(nombre)
        cantidad +=1
print(cantidad)

#¿Cuántos alumnos tienen teléfono pertenecientes a Rosario?
for nombre, apellido, telefono, email in alumnos:
    if telefono[0:3]=='341':
        print(telefono)

#¿Cuántos mails no son @gmail.com?
for nombre, apellido, telefono, email in alumnos:
    if "gmail.com" not in email:
        print(email)

