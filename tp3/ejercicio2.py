#2. Dados 3 lados de un triángulo, informar si el mismo es equilátero, isósceles o escaleno.

#Datos
lado1 = float (input("Ingrese la longitud del lado 1: "))
lado2 = float(input ("Ingrese la longitud del lado 2: "))
lado3 = float(input ("Ingrese la longitud del lado 3: "))
#Procesamiento
if lado1 == lado2 and lado2 == lado3:
    tipo = "equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo = "isósceles"    
else:
    tipo = "escaleno"    
#Salida
print("El triángulo es:", tipo)