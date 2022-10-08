import csv
from classes import *

lista_Cont = [
    ["normal", ["solida", ], ["liquida", ], ["gas", ]],
    ["refrigerado", ["solida", ], ["liquida", ], ["gas", ]],
    ["inflamable", ["solida", ], ["liquida", ], ["gas", ]]]

lista_Vh = [[],[],[]]
# Leer el archivo csv (retorna una matriz con cada producto como una lista
#                        con sus respectivos atributos). 
# 										Todos los valores	retornados son strings
def read_csv(x):
    with open(x, 'r') as c:
        line = csv.reader(c)
        lista = list(line)
    return lista

# Asigna la cantidad de contenedores a cada tipo de contenedor
# (pesos_normales, pesos_refrigerados, pesos_inflamables)


def lista_Contenedores(lista, lista_Cont):
	cont_Totales = 0
	for i in range(len(lista)):
		for x in range(len(lista_Cont)):
			if lista[i][2] == lista_Cont[x][0]:
				for j in range(len(lista_Cont[0])):
					if lista[i][3] == lista_Cont[x][j][0]:
							objeto = Producto()
							objeto.atributos(lista[i][2], lista[i][3],
																	int(lista[i][4]))
							print(objeto.cont_G + (objeto.cont_P)/2)
							cont_Totales += ( objeto.cont_G + (objeto.cont_P)/2)
							lista_Cont[x][j].append(objeto)
							break
			else:
				continue
	print(cont_Totales)
	return cont_Totales

def lista_vehiculos(cont_Totales):
	
	pass


if __name__ == "__main__":
	lista = read_csv("MOCK_DATA.csv")
	lista_Contenedores(lista, lista_Cont)
