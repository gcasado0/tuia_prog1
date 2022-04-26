'''
3.3 Solicitar una letra y detecte si es una vocal.
'''

x = input("Ingresa una letra: ") #Todo: tengo que validar que sea una letra?
x = x.lower()

if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    print("Es una vocal")
else:
    print("No es una vocal")
