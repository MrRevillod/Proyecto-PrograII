from proyectov3 import *
from classes import *

def prints_Enunciado_1(lista_Vh):
	suma_Total_cont= 0; costo_total = 0
	for x in range(len(lista_Vh)):
		totales_Parciales = 0
		for y in range(len(lista_Vh[x])):
			suma_Total_cont += 1
			costo_total += lista_Vh[x][y].costo
			totales_Parciales += lista_Vh[x][y].costo
		if len(lista_Vh[x]) != 0:
			print(f"El costo total para los {lista_Vh[x][0].nom_Vh}\
							es : {totales_Parciales}") # Costos parciales por vehiculo
	print("Cantidad total de Vehiculos : ", suma_Total_cont) # cantidad total
	# de vehiculos
	print(f"El costo total del transporte es : {costo_total}") # costo
	# total del transporte de todos los vehiculosy sus contenedores
	for x in range(len(lista_Vh)):
		for y in range(len(lista_Vh[x])):
			lista_Vh[x][y].prints_Enunciado_1()


if __name__ == "__main__":
	lista = read_csv("MOCK_DATA.csv")
	lista_Contenedores(lista, lista_Cont)
	cant_Vh = cant_Vh(cont_Totales(lista_Cont)[0])
	lista_Vehiculos = Dep_en_Vh(cant_Vh, cont_Totales(lista_Cont)[1], lista_Vh)
	for index in range(len(lista_Vehiculos)):
		jsonconvert(index, lista_Vehiculos, nom_Vh)
	prints_Enunciado_1(lista_Vh)
