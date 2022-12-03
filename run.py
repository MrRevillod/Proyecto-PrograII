from main import *

def run_program(lista_Cont, lista_Vh):
	insert_to_db(read_csv("MOCK_DATA.csv"))
	lista_Contenedores(get_list_to_db(), lista_Cont)
	num_Total_Depositos, lista_All_Dep = cont_Totales(lista_Cont)
	num_Vh = cant_Vh(num_Total_Depositos)
	Dep_en_Vh(num_Vh, lista_All_Dep, lista_Vh)

run_program(lista_Cont, lista_Vh)