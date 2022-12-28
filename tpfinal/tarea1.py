import csv
import numpy as np

def obtener_extremos_por_tipo_habitacion(filter_room_type):
  print("")
  print("Filtro por:",filter_room_type)
  
  with open('/home/gcasado0/proyectos/tuia_prog1/tpfinal/listings.csv', newline='') as File:
    reader = csv.reader(File, delimiter=',')
    num_row = 0
    descartados = 0
    agrupamiento={}
    for row in reader:
      num_columns = 0
      
      if(num_row>0):#salto el encabezado
        #datos.append(row[27]) #barrio
        distrito = row[28] #distrito
        room_type = row[32] #room_type
        price = row[39][1:].replace(',','') #39 es el indice del precio
        camas = row[37] #beds
        if (price!='' and camas!='' and room_type==filter_room_type):
          ratio_price_bed = float(price)/float(camas)    
          #print('price/bed:', ratio_price_bed)
          if (distrito in agrupamiento):
              agrupamiento[distrito].append(ratio_price_bed)
          else:
              lista = []
              lista.append(ratio_price_bed)
              agrupamiento[distrito] = lista
        else:
          descartados += 1

      num_row += 1

  print("")
  print("Cantidad total de datos: ", num_row-1)
  print("Cantidad de datos descartados: ", descartados)
  print("")


  agrupamiento_precio_promedio = {}
  for grupo, valores in agrupamiento.items():
    n = 1
    output = [x for x in valores if abs(x - np.mean(valores)) < np.std(valores) * n]
    cantidad = len(output)
    suma = sum(output)
    minimo = min(output)
    maximo = max(output)
    promedio = suma/cantidad
    agrupamiento_precio_promedio[grupo] = promedio
    print("Cantidad datos por distrito", grupo,": ", cantidad, "- min,prom,max:", round(minimo),",",round(promedio),",",round(maximo))
 

obtener_extremos_por_tipo_habitacion("Entire home/apt")
obtener_extremos_por_tipo_habitacion("Private room")
obtener_extremos_por_tipo_habitacion("Hotel room")
obtener_extremos_por_tipo_habitacion("Shared room")