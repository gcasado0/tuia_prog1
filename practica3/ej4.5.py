'''
4.4 Contar e informar los n´umeros m´ultiplos de 2 o 3 que hay entre 1 y 100. Verificar el resultado
'''

multiplos_2 = 0
multiplos_3 = 0
multiplos_2y3 = 0

for x in range(1,101):
    if (x%2==0) and not((x%3==0)):
        print(x, " -> Es multiplo de 2")
        multiplos_2 += 1
    if (x%3==0) and not(x%2==0):
        print(x, " -> Es multiplo de 3")
        multiplos_3 += 1
    if (x%3==0) and (x%2==0):        
        print(x, " -> Es multiplo de 2 y 3")
        multiplos_2y3 +=1
    if (not ((x%2==0) or (x%3==0))):
        print(x)

print("Total multiplos de 2: " , multiplos_2)
print("Total multiplos de 3: " , multiplos_3)
print("Total multiplos de 2y3: " , multiplos_2y3)