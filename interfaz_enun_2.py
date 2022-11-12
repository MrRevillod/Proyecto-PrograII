from tkinter import *
from proyectov3 import *

lis_form_1 = [
	["Selecciona una de las siguientes opciones :"],
	["1 .- Cantidad total de vehículos"],
	["2 .- Cantidad total de cada vehículo"],
	["3 .- Selecciona uno de los vehículos a continuación :"]
]

vhs = ["trenes", "aviones", "camiones"]

lista_labels = []

#========================================================================#
#====================== Limpiar ventana de Widgets ======================#
#========================================================================#

def clean_wid(lis_wid):
	for x in range(len(lis_wid)):
		lis_wid[x].destroy()

#========================================================================#
#================ indice 1 : Cantidad total de vehiculos ================#
#========================================================================#

def total_Vhs(lista_Vh):
	suma_total = 0
	for x in range(len(lista_Vh)):
		suma_total += len(lista_Vh[x])
	window = Toplevel()
	Label(window, 
				text= "La cantidad total de vehiculos para "
							"transportar todos los productos es : "
							f"{suma_total}").pack()

#========================================================================#
#============ indice 2 :Cantidad total de cada tipo de vehiculo==========#
#========================================================================#

def total_Por_Vh(lista_Vh, vhs):
	img_tren = PhotoImage(file= "tren.png")
	img_avion = PhotoImage(file= "avion.png")
	img_camion = PhotoImage(file= "camion.png")
	lista_img = [img_tren, img_avion, img_camion]
	window = Toplevel()
	for x in range(len(vhs)):
		Label(window, text= f"La cantidad total de {vhs[x]} es : {len(lista_Vh[x])}",
					width= 30, height= 10).grid(row=0, column=x)
		Label(window, image= lista_img[x]).grid(row= 1, column= x)

#========================================================================#
#================ indice 3 :Al seleccionar un vehiculo ==================#
#========================================================================#

def select_vh(root, lis_Wid, lista_Vh, vhs):
	clean_wid(lis_Wid)
	lbl_sel = Label(root, text= "Elige un vehiculo : ", width= 100,
	height= 5)
	lbl_sel.grid(row= 0,column=0, columnspan= 4)

	# barco = Button(root, text= "Barco", width= 30, height= 2)
	# barco.grid(row= 1, column= 0)

	tren = Button(root, text= "Tren", width= 30, height= 2,
	command= lambda : vh_selected(0, root,lista_Vh, vhs, lis_Wid_2))
	tren.grid(row= 1, column= 0)

	avion = Button(root, text= "Avion", width= 30, height= 2,
	command= lambda : vh_selected(1, root,lista_Vh, vhs, lis_Wid_2))
	avion.grid(row= 1, column= 1)

	camion = Button(root, text= "Camion", width= 30, height= 2,
	command= lambda : vh_selected(2, root,lista_Vh, vhs, lis_Wid_2))
	camion.grid(row= 1, column= 2)

	lis_Wid_2 = [lbl_sel, tren, avion, camion]

#========================================================================#
#====== Mostrar Cantidad de vehiculos para el tipo seleccionado =========#
#========================================================================#

def vh_selected(index, root, lista_Vh, vhs, lis_Wid_2):
	cant_Vh = len(lista_Vh[index])
	var_Response = IntVar()
	lbl_quest = Label(root,
	text= f"Hay {cant_Vh} {vhs[index]}\nQue numero de vehiculo deseas elegir: "
	, justify= CENTER)
	lbl_quest.grid(row= 2, column= 1)
	lis_Wid_2.append(lbl_quest)
	
	response = Entry(root, textvariable= var_Response)
	response.grid(row= 3, column= 1)
	lis_Wid_2.append(response)

	but_get = Button(root, text= "Obtener datos del vehiculo",
	command= lambda : print_Vh(root,
														index,
														var_Response.get(),
														lista_Vh,
														lis_Wid_2))
	but_get.grid(row= 4, column= 1)
	lis_Wid_2.append(but_get)

def print_Vh(root, index, index_2, lista_Vh, lis_Wid_2):
	clean_wid(lis_Wid_2)
	vh = lista_Vh[index][index_2]

	vh.punto_3_1(root)
	vh.punto_3_2(root)
	vh.punto_3_3(root)
	vh.punto_3_4(root)
	vh.punto_3_5(root)

#========================================================================#
#==== Seleccionar las funcionas correspondientes a las seleccionadas ====#
#========================================================================#

def form_1 (option, lista_Vh, vhs, root, lis_Wid):
	if option == 1:
		total_Vhs(lista_Vh)
	elif option == 2:
		total_Por_Vh(lista_Vh, vhs)
	elif option == 3:
		select_vh(root, lis_Wid, lista_Vh, vhs)

#========================================================================#
#================ indice 4.1 :Costo total de transporte =================#
#========================================================================#

def costo_Transporte(lista_Vh):
	total_Transporte = 0
	for x in range(len(lista_Vh)):
		total_Transporte += lista_Vh[x].costo
	print(total_Transporte)

#========================================================================#
#================ indice 4.1 :Costo total de transporte =================#
#========================================================================#

#========================================================================#
#=================== Inicialización de funciones ========================#
#========================================================================#

if __name__ == "__main__":
	lis = read_csv("MOCK_DATA.csv")
	insert_to_db(lis)
	lista = get_information_to_db()
	lista_Contenedores(lista, lista_Cont)
	cant_Vhs = cant_Vh(cont_Totales(lista_Cont)[0])
	lista_Vehiculos = Dep_en_Vh(cant_Vhs, cont_Totales(lista_Cont)[1], lista_Vh)

#========================================================================#
#==================== Inicialización de Tkinter =========================#
#========================================================================#

root = Tk()
root.title("Proyecto de Programación II - INFO1123")

#========================================================================#
#============= Botones y Preguntas Formulario principal =================#
#========================================================================#

var_Form = IntVar()

quest_1 = Label(root, text= lis_form_1[0][0])
quest_1.pack(anchor= W)

enun1 = Radiobutton(root, text= lis_form_1[1][0], value= 1, variable= var_Form)
enun1.pack(anchor= W)

enun2 = Radiobutton(root , text= lis_form_1[2][0], value= 2, variable= var_Form)
enun2.pack(anchor= W)

enun3 = Radiobutton(root, text= lis_form_1[3][0], value= 3, variable= var_Form)
enun3.pack(anchor= W)

send_Select = Button(root, text= "Enviar", 
										command=lambda : form_1(var_Form.get(),
																						lista_Vh,
																						vhs,
																						root,
																						lista_widgets))
send_Select.pack()

lista_widgets = [quest_1, enun1, enun2, enun3, send_Select]

root.mainloop()