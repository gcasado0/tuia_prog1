#2. Dados 3 lados de un triángulo, informar si el mismo es equilátero, isósceles o escaleno.

#datos
lado1 = float(input("Ingrese el lado 1: "))
lado2 = float(input("Ingrese el lado 2: "))
lado3 = float(input("Ingrese el lado 3: "))
#procesamiento
if lado1 == lado2 and lado2 == lado3:
    tipo = "equilátero"
elif lado1 == lado2 or lado1 == lado3:
    tipo = "isósceles"    
else:
    tipo = "escaleno"    
#salida
print("El triángulo es:", tipo)