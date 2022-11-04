from tkinter import *
from proyectov3 import *

lis_form_1 = [
	["Selecciona una de las siguientes opciones :"],
	["1 .- Cantidad total de vehículos"],
	["2 .- Cantidad total de cada vehículo"],
	["3 .- Selecciona uno de los vehículos a continuación :"]
]

vhs = ["trenes", "aviones", "camiones"]

def total_Vhs(lista_Vh):
	suma_total = 0
	for x in range(len(lista_Vh)):
		suma_total += len(lista_Vh[x])
	window = Toplevel()
	Label(window, 
				text= "La cantidad total de vehiculos para "
							"transportar todos los productos es : "
							f"{suma_total}").pack()

def total_Por_Vh(lista_Vh, vhs):
	window = Toplevel()
	for x in range(len(vhs)):
		Label(window, text= f"La cantidad total de {vhs[x]} es : {len(lista_Vh[x])}",
					width= 30, height= 10).grid(row=0, column=x)

def form_1 (option, lista_Vh, vhs):
	if option == 1:
		total_Vhs(lista_Vh)
	elif option == 2:
		total_Por_Vh(lista_Vh, vhs)

if __name__ == "__main__":
	lis = read_csv("MOCK_DATA.csv")
	insert_to_db(lis)
	lista = get_information_to_db()
	lista_Contenedores(lista, lista_Cont)
	cant_Vhs = cant_Vh(cont_Totales(lista_Cont)[0])
	lista_Vehiculos = Dep_en_Vh(cant_Vhs, cont_Totales(lista_Cont)[1], lista_Vh)

root = Tk()
root.title("Proyecto de Programación II - INFO1123")
var_Form_1 = IntVar()


quest_form_1 = Label(root, text= lis_form_1[0][0])
quest_form_1.pack(anchor= W)

enun1 = Radiobutton(root, text= lis_form_1[1][0], value= 1, variable= var_Form_1)
enun1.pack(anchor= W)

enun2= Radiobutton(root , text= lis_form_1[2][0], value= 2, variable= var_Form_1)
enun2.pack(anchor= W)

enun3= Radiobutton(root, text=lis_form_1[3][0], value= 3, variable= var_Form_1)
enun3.pack(anchor= W)

send_Select = Button(root, text= "Enviar", 
										command=lambda : form_1(var_Form_1.get(),
																						lista_Vh,
																						vhs)).pack()

root.mainloop()