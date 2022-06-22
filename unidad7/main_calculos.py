from raices import cuadratica

print('1. raiz cuadrada')
print('2. raiz de n')
print('3. resolvente')
f = int(input('Ingrese la función que desea utilizar: \n'))

if(f == 1):
  a = int(input('Ingrese el radicando: '))
  #print(raices.raiz_cuadrada(a))

elif(f == 2):
  a = int(input('Ingrese el radicando: '))
  n = int(input('Ingrese el indice: '))
  #print(raices.raiz(a,n))

else:
  A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
  B = int(input("Ingrese el coeficiente de la variable lineal\n"))
  C = int(input("Ingrese el término independiente\n"))

  r1,r2 = cuadratica(A,B,C)

  print(r1)
  print(r2)