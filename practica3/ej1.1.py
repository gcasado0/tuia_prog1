#1.1 Dada la base B y la altura H de un rect´angulo, informar el ´area y el per´ımetro.

#entrada
base = float(input("Base del rectangulo: "))
altura = float(input("Altura del recturango: "))

#procesamiento
perimetro = 2 * base + 2 * altura
area = base * altura

#salida
print("Perimetro = ",perimetro)
print("Area = ", area)
