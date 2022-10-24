import csv
from classes import *
import json as json

lista_Cont = [
    ["normal", ["solida", ], ["liquida", ], ["gas", ]],
    ["refrigerado", ["solida", ], ["liquida", ], ["gas", ]],
    ["inflamable", ["solida", ], ["liquida", ], ["gas", ]]]

lista_Vh = [[],[],[]]

def read_csv(x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
    return lista

def lista_Contenedores(lista, lista_Cont):
	peso_Max_Por_Tipo_Cont = [["normal",24000], ["refrigerado", 20000], ["inflamable",22000]]

	for i in range(len(lista)):
		peso_Prod = int(lista[i][4])

		for x in range(len(lista_Cont)):
			if lista[i][2] == lista_Cont[x][0]:

				for j in range(len(lista_Cont[0])):
					if lista[i][3] == lista_Cont[x][j][0]:

						for t in range(len(peso_Max_Por_Tipo_Cont)):
							if lista[i][2] == peso_Max_Por_Tipo_Cont[t][0]:

								pesomax = peso_Max_Por_Tipo_Cont[t][1]
								arr = cant_Cont(peso_Prod, pesomax)

								for g in range(arr[0]):
									obj = Deposito()
									obj.atributos(int(lista[i][0]), lista[i][1], lista[i][2], lista[i][3], pesomax, "grande")
									lista_Cont[x][j].append(obj)

								if arr[1][1] != 0:
									if len(arr) == 3:
										obj = Deposito()
										obj.atributos(int(lista[i][0]), lista[i][1], lista[i][2], lista[i][3], arr[1][1], "pequeño")
										lista_Cont[x][j].append(obj)
									else:
										obj = Deposito()
										obj.atributos(int(lista[i][0]), lista[i][1], lista[i][2], lista[i][3], arr[1][1], "grande")
										lista_Cont[x][j].append(obj)
						break
			else:
				continue
	return

def cant_Cont(pesox, pesomax):
	cont_G_llenos = 0; cont_G = 0; cont_P = 0

	if pesox >= pesomax:
		cont_G_llenos += pesox//pesomax
		resto = pesox % pesomax

		if resto > (pesomax/2):
			cont_G += 1
			lista_G = [cont_G, resto]
			return [cont_G_llenos, lista_G]

		else:
			cont_P += 1
			lista_P = [cont_P, resto]
			return [cont_G_llenos, lista_P, "algo"]

	elif pesox > (pesomax/2) :
		cont_G += 1
		lista_G = [cont_G, pesox]
		return [cont_G_llenos, lista_G]

	else:
		cont_P += 1
		lista_P = [cont_P, pesox]
		return [cont_G_llenos, lista_P, "algo"]

def cont_Totales(lista_Cont):
	cantidad_Total = float(0)

	for x in range(len(lista_Cont)):
		for y in range(1, len(lista_Cont[0])):
			for j in range(1, len(lista_Cont[x][y])):

				if lista_Cont[x][y][j].porte == "pequeño":
					cantidad_Total += 0.5

				elif lista_Cont[x][y][j].porte == "grande":
					cantidad_Total += 1

	return cantidad_Total

def cant_Vh(cont_Totales):

	tren = 0 ; avion = 0 ; camion = 0

	if cont_Totales >= 250:
		tren += cont_Totales // 250
		resto = cont_Totales % 250

		if resto >= 10:
			avion += resto // 10
			resto_menor = avion % 10

			if resto_menor <= 1:
				camion += 1
				return [[tren], [avion], [camion, resto_menor]]
			else:
				avion += 1
				return [[tren], [avion, resto_menor], [camion]]

		elif resto <= 1:
			camion += 1
			return [[tren], [avion], [camion, resto]]
		else:
			avion += 1
			return [[tren], [avion, resto], [camion]]

	elif cont_Totales >= 10:
		avion += cont_Totales// 10
		resto = cont_Totales % 10

		if resto <= 1:
			camion += 1
			return [[tren], [avion], [camion, resto]]
		else:
			avion += 1
			return [[tren], [avion, resto], [camion]]

	elif cont_Totales <= 1:
		camion += 1
		return [[tren], [avion], [camion, cont_Totales]]

	else:
		avion += 1
		return [[tren], [avion,cont_Totales], [camion]]

def assing_Vh(lista_Vhs, lista_Vh):
	""" print(lista_Vhs[0][0]) """

	for x in range(len(lista_Vhs)):
		if x == 0 and len( lista_Vhs[x] ) != 2:
			for t in range(int( lista_Vhs[0][0] )):
				obj = Vehiculos()
				obj.assign_atr(250)
				lista_Vh[x].append(obj)

		elif x == 1 and len( lista_Vhs[x] ) != 2:
			for y in range(int(lista_Vhs[1][0])):
				obj = Vehiculos()
				obj.assign_atr(10)
				lista_Vh[x].append(obj)

		elif x == 2 and len( lista_Vhs[x] ) != 2:
			for j in range(int(lista_Vhs[2][0])):
				obj = Vehiculos()
				obj.assign_atr(1)
				lista_Vh[x].append(obj)

		elif len(lista_Vhs[x]) == 2:
			obj = Vehiculos()
			obj.assign_atr(lista_Vhs[x][1])
			lista_Vh[x].append(obj)
			

	
def jsonconvert(lista_Cont):
    lista = [[],[]]
    with open("contenedores.json", "w") as file:
        for x in range(len(lista_Cont)):
            for y in range(1, len(lista_Cont[0])):
                for j in range(1, len(lista_Cont[x][y])):
                    lista[0].append(lista_Cont[x][y][j].__dict__)
        json.dump(lista[0], file, indent=7)


""" Estructura JSON:
        
        {   
            "person":  [  
                {
                    "Primer_Nombre":"Oscar",
                    "Primer_Apellido":"Mellado",
                    "email":"omellado@dwm.nz",
                    "Asunto":"hola"
                },
                {
                    "Primer_Nombre":"Luciano",
                    "Primer_Apellido":"Revillod",
                    "email":"lrevillod@dwm.nz",
                    "Asunto":"holi"
                }
            ]
        }     
"""

if __name__ == "__main__":
	lista = read_csv("MOCK_DATA.csv")
	lista_Contenedores(lista, lista_Cont)
	assing_Vh(cant_Vh(cont_Totales(lista_Cont)), lista_Vh)
	jsonconvert(lista_Cont)
	
	