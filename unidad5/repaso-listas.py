lista = list("1234")
print(lista)

tupla = (1,2,3,4,5)
print(list(tupla))

lista=list(range(5))
print(lista)

alumno = [7 , " Jose ", 24 , 2022]
alumno [0:2] = [2 , " Manuel "]
print(alumno)

lista = [1 , 2 , 3]
lista . insert (2 , 15)
print(lista)

lista_invertida = []
for x in lista:
    lista_invertida.insert(0,x)

print(lista_invertida)
lista_nueva = lista + lista_invertida
print(lista_nueva)
lista_nueva.remove(3) #elimina la primera ocurrencia del elemento
print(lista_nueva)
lista_nueva.pop(1) #elimina el segundo elemento
print(lista_nueva)
print(len(lista_nueva))
print(lista_nueva.index(15)) #devuelve la primera posicion del elemento si la encuentra
print(10 in lista_nueva)
lista_nueva.sort()
print(lista_nueva)

lista = ['a', 'b', 'c', 'd', 'e']

for elemento in lista :
    print(elemento)

for i in range (len (lista)):
    print(lista[i])

for index , value in enumerate(lista):
    print(index,value)

x=list(enumerate(lista))
print(x)

print(lista.count('b'))
