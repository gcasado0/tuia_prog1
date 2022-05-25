dicc={"Nombre":"Matías","Telefono":"3411038003","Edad":23}
print(dicc)
print(dicc["Nombre"])

dicc1=dict([('jorge',4139),('guido',4127),('hugo',4098)])
print(dicc1)

dicc2=dict([['jorge',4139],['guido',4127],['hugo',4098]])
print(dicc2)

cumples={}
cumples[(20,2)] = "Luciano"
cumples[(18,8)] = "Gustavo"
print(cumples)
print(cumples.get((4,7)))

print(list(dicc))
print(dicc.keys())
print(dicc.values())
print(dicc.items())

for x in dicc:
    print(x)

for x in dicc.keys():
    print(x)

for x in dicc.values():
    print(x)    

for x,y in dicc.items():
    print(x,y)  

print("Nombre" in dicc)

x=dicc.pop("Telefono")
print(dicc)
print(x)

x=dicc.popitem()
print(dicc)
print(x)
dicc.update({"Telefono": 341116677,"Edad": 44, "Nombre": "Matias Jorge"})
print(dicc)