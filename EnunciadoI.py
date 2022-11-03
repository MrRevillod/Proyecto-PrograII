from main import *
from classes import *

if __name__ == "__main__":
	lista = read_csv("MOCK_DATACHICO.csv")
	lista_Contenedores(lista, lista_Cont)
	cant_Vh = cant_Vh(cont_Totales(lista_Cont)[0])
	lista_Vehiculos = Dep_en_Vh(cant_Vh, cont_Totales(lista_Cont)[1], lista_Vh)
	for index in range(len(lista_Vehiculos)):
		jsonconvert(index, lista_Vehiculos, nom_Vh)

#Json son creados para la interfaz grafica
#Mock_data.csv fue acortado (solo 15 productos)