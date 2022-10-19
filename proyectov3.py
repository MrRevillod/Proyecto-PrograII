import csv
import json
from classes import *

# lista ordenada para juntar y organizar los contenedores por tipo y masa
lista_Cont = [
    ["normal", ["solida", ], ["liquida", ], ["gas", ]],
    ["refrigerado", ["solida", ], ["liquida", ], ["gas", ]],
    ["inflamable", ["solida", ], ["liquida", ], ["gas", ]]]

# cantidad de vehiculos [0] = tren, [1] =avion, [2] = camion
lista_Vh = [[],[],[]]
# Leer el archivo csv (retorna una matriz en la que cada sublista
# 											corresponde a un producto con todos
# 											sus atributos). retorna todo como string
def read_csv(x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
    return lista

# Crea cada instancia de contenedor y los agrega a la lista de contenedores
# según sus características (tipo de contenedor y masa del producto).
def lista_Contenedores(lista, lista_Cont):
	peso_Max_Por_Tipo_Cont = [
							["normal",24000],
							["refrigerado", 20000],
							["inflamable",22000]]
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
									obj.atributos(int(lista[i][0]), lista[i][1],
																lista[i][2], lista[i][3],
																pesomax, "grande")
									lista_Cont[x][j].append(obj)
								if arr[1][1] != 0:
									if len(arr) == 3:
										obj = Deposito()
										obj.atributos(int(lista[i][0]), lista[i][1],
																	lista[i][2], lista[i][3],
																	arr[1][1], "pequeno")
										lista_Cont[x][j].append(obj)
									else:
										obj = Deposito()
										obj.atributos(int(lista[i][0]), lista[i][1],
																	lista[i][2], lista[i][3],
																	arr[1][1], "grande")
										lista_Cont[x][j].append(obj)
						break
			else:
				continue
	return

# Esta función se utiliza para sacar la cantida de contenedores grandes
# llenos, grandes con resto y/o pequeños con restos, esta implementada
# en la función lista_Contenedores.
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
			return [cont_G_llenos, lista_P, "pequeño"]
	elif pesox > (pesomax/2) :
		cont_G += 1
		lista_G = [cont_G, pesox]
		return [cont_G_llenos, lista_G]
	else:
		cont_P += 1
		lista_P = [cont_P, pesox]
		return [cont_G_llenos, lista_P, "pequeño"]

# cantidad de contenedores considerando que los pequeños ocupan la
# mitad del espacio que los grandes, por lo que en vez de contar
# como un entero, cada uno vale 0.5 respecto de uno grande
def cont_Totales(lista_Cont):
	cantidad_Total = float(0)
	for x in range(len(lista_Cont)):
		for y in range(1, len(lista_Cont[0])):
			for j in range(1, len(lista_Cont[x][y])):
				if lista_Cont[x][y][j].porte == "pequeno":
					cantidad_Total += 0.5
				elif lista_Cont[x][y][j].porte == "grande":
					cantidad_Total += 1
				# if lista_Cont[x][y][j].id_Prod == 100:
				# 	print(lista_Cont[x][y][j].tipo_Carga)
	return cantidad_Total

# retorna una lista con la cantidad de vehiculos, si hay un resto
# se le asigna al vehiculo correspondiente, esto se utiliza en la
# función Dep_en_Vh.
def cant_Vh(cont_Totales):
	# barco = 0 (este se excluye porque en ningun punto su rentabilidad
	# 						queda por encima de todos los vehiculos).
	tren = 0
	avion = 0
	camion = 0
	lista = [[tren], [avion], [camion]]
	if cont_Totales >= 250:
		tren += cont_Totales // 250
		resto = cont_Totales % 250
		if resto >= 10:
			avion += resto // 10
			resto_menor = avion % 10
			if resto_menor <= 1:
				camion += 1 ; lista[2].append(resto_menor)
			else:
				avion += 1 ; lista[1].append(resto_menor)
		elif resto <= 1:
			camion += 1 ; lista[2].append(resto)
		else:
			avion += 1 ; lista[1].append(resto)
	elif cont_Totales >= 10:
		avion += cont_Totales// 10
		resto = cont_Totales % 10
		if resto <= 1:
			camion += 1 ; lista[2].append(resto)
		else:
			avion += 1 ; lista[1].append(resto)
	elif cont_Totales <= 1:
		camion += 1 ; lista[2].append(cont_Totales)
	else:
		avion += 1 ; lista[1].append(cont_Totales)
		return lista

# Crea las instancias de vehiculos y los agrega a la lista_Vh,
# tambien para cada instancia agrega los contenedores correspondientes
# a cada vehiculo en concreto.
def Dep_en_Vh(cant_Vhs, lista_Cont, lista_Vh):
	cont_maximos = [250, 10, 1]
	for k in range(len(cant_Vhs)):
		if len(cant_Vhs[k]) == 2:
			# obj = Vehiculos()
			# obj.assign_atr(cant_Vhs[x][1]) # falta agregar los contenedores
																			# correspondientes al vehiculo
			# lista_Vh[k].append(obj)
			pass
		if cant_Vhs[k][0] > 0:
			for r in range((int(cant_Vhs[k][0]))):
				vh = Vehiculos()
				lista = []
				for x in range(len(lista_Cont)):
					for y in range(1, len(lista_Cont[0])):
						for j in range(1, len(lista_Cont[x][y])):
							deposito = lista_Cont[x][y][j]
							if count == 10:
								break
							lista.append(deposito)
							count += 1
						break
					break
				print(lista, "algo")
				vh.assign_atr(cont_maximos[k], lista)
				lista_Vh[k].append(vh)

# Crea el archivo json para luego utilizarlo de parte del javascript
def jsonconvert(lista_Cont,lista_Vh):
	lista = [[],[]]
	with open("contenedores.json", "w") as file:
		for x in range(len(lista_Cont)):
			for y in range(1, len(lista_Cont[0])):
				for j in range(1, len(lista_Cont[x][y])):
					lista[0].append(lista_Cont[x][y][j].__dict__)
		json.dump(lista[0], file, indent=2)

	with open("vehiculos.json", "w") as file:
		for t in range(len(lista_Vh)):
			for g in range(len(lista_Vh[t])):
				lista[1].append(lista_Vh[t][g].__dict__)
		json.dump(lista[1], file, indent=3)

if __name__ == "__main__":
	lista = read_csv("MOCK_DATA.csv")
	lista_Contenedores(lista, lista_Cont)
	Dep_en_Vh(cant_Vh(cont_Totales(lista_Cont)), lista_Cont, lista_Vh)
	# jsonconvert(lista_Cont, lista_Vh)
