import csv
path = '/home/gcasado0/proyectos/tuia_prog1/tpfinal/'

with open(path + 'listings.csv', newline='') as File:
    reader = csv.reader(File, delimiter=',')
    num_row = 1
    barrios={}
    for row in reader:
        num_columns = 0
        datos = []
        datos.append(row[27])
        datos.extend(row[31:38])
        datos.append(row[39])
        print('Barrio: ', datos[0])
        print('Datos', datos)
        if(num_row>1):
            price = datos[8][1:]
            if (price!='' and datos[7]!=''):
                ratio_price_bed = round(float(price)/float(datos[7]),2)            
                print('price/bed:', ratio_price_bed)
                if (datos[0] in barrios):
                    barrios[datos[0]].append(ratio_price_bed)
                else:
                    lista = []
                    lista.append(ratio_price_bed)
                    barrios[datos[0]] = lista

        print("")
        if(num_row == 500): #solo leemos n rows
            break;
        num_row += 1
    
    print(barrios)

    for barrio, valores in barrios.items():
        cantidad = len(valores)
        suma = 0
        for x in valores:
            suma += x
        promedio = suma/cantidad
        print(barrio, "-> promedio: ", round(promedio))
