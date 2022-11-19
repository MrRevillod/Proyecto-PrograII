from kernel import *
from tkinter import *

lis_Form_1 = [
	["Selecciona una de las siguientes opciones :"],
	["1 .- Cantidad total de vehículos"],
	["2 .- Cantidad total de cada vehículo"],
	["3 .- Selecciona uno de los vehículos a continuación : "],
	["4 .- Costos totales de transporte"]
]

vhs = ["trenes", "aviones", "camiones"]

#========================================================================#
#==================== Iniciar ventana principal tkinter =================#
#========================================================================#

def init_tk():
	root = Tk()
	root.title("Proyecto de Programación II - INFO1123")
	root.geometry('1000x600+250+250')
	root['bg'] = '#0088b6'
	return root

#========================================================================#
#==================== Formulario principal interfaz =====================#
#========================================================================#

def inter_form_1(root, lis_Form_1, lista_Vh, vhs):
	var_Form = IntVar()

	quest_1 = Label(root, text= lis_Form_1[0][0], font=("Arial", 15), bg= "#0088b6")
	quest_1.pack(anchor= CENTER)

	enun1 = Radiobutton(root, text= lis_Form_1[1][0], value= 1, bg= "#0088b6",
											variable= var_Form, font=("Arial", 13))
	enun1.pack(anchor= CENTER)

	enun2 = Radiobutton(root , text= lis_Form_1[2][0], value= 2, bg= "#0088b6",
											variable= var_Form, font=("Arial", 13))
	enun2.pack(anchor= CENTER)

	enun3 = Radiobutton(root, text= lis_Form_1[3][0], value= 3, bg= "#0088b6",
											variable= var_Form, font=("Arial", 13))
	enun3.pack(anchor= CENTER)

	enun4 = Radiobutton(root, text= lis_Form_1[4][0], value= 4, bg= "#0088b6",
											variable= var_Form, font=("Arial", 13))
	enun4.pack(anchor= CENTER)

	send_Select = Button(root, text= "Enviar", font=("Arial", 13), bg= "#0088b6",
											command=lambda : form_1(var_Form.get(),
																							lista_Widgets,
																							root,
																							lista_Vh,
																							vhs))
	send_Select.pack()

	lista_Widgets = [quest_1, enun1, enun2, enun3, enun4, send_Select]

#========================================================================#
#==== Seleccionar las funcionas correspondientes a las seleccionadas ====#
#========================================================================#

def form_1 (option, lis_Wid, root, lista_Vh, vhs):
	if option == 1:
		total_Vhs(root, lis_Wid, lista_Vh)
	elif option == 2:
		total_Por_Vh(root, lis_Wid, lista_Vh, vhs)
	elif option == 3:
		select_vh(root, lis_Wid, lista_Vh, vhs)
	elif option == 4:
		indice_4_1(root, lis_Wid, lista_Vh)
		indice_4_2(root, lista_Vh, vhs)

#========================================================================#
#================ indice 1 : Cantidad total de vehiculos ================#
#========================================================================#

def total_Vhs(root, lis_Wid, lista_Vh):
	clean_wid(lis_Wid)
	suma_total = 0
	for x in range(len(lista_Vh)):
		suma_total += len(lista_Vh[x])
	lbl = Label(root, bg= "#0088b6",
							font= ("Arial", 15),
							text= "La cantidad total de vehiculos para "
										"transportar todos los productos es : "
										f"{suma_total}")
	lbl.grid(column=0, row=0, padx=10, pady= 10)

#========================================================================#
#============ indice 2 :Cantidad total de cada tipo de vehiculo==========#
#========================================================================#

def total_Por_Vh(root, lis_Wid, lista_Vh, vhs):
	clean_wid(lis_Wid)
	img_tren = PhotoImage(file= r"C:\xampp\htdocs\Proyecto-PrograII\img\tren.png")
	img_avion = PhotoImage(file= r"C:\xampp\htdocs\Proyecto-PrograII\img\avion.png")
	img_camion = PhotoImage(file= r"C:\xampp\htdocs\Proyecto-PrograII\img\camion.png")
	lista_img = [img_tren, img_avion, img_camion]
	for x in range(len(vhs)):
		lbl_text = Label(root, text= f"La cantidad total de {vhs[x]} es : {len(lista_Vh[x])}",
					width= 30, height= 10, bg= "#0088b6")
		lbl_text.grid(row=0, column=x)

		lbl_img = Label(root, image= lista_img[x])
		lbl_img.grid(row= 1, column= x)
	root.mainloop()


#========================================================================#
#================ indice 3 :Al seleccionar un vehiculo ==================#
#========================================================================#

def select_vh(root, lis_Wid, lista_Vh, vhs):
	clean_wid(lis_Wid)
	lbl_sel = Label(root, text= "Elige un vehiculo : ", width= 100, bg= "#0088b6",
	height= 5, font=("Arial", 13))
	lbl_sel.grid(row= 0,column=0, columnspan= 4)

	# barco = Button(root, text= "Barco", width= 30, height= 2)
	# barco.grid(row= 1, column= 0)

	tren = Button(root, text= "Tren", width= 30, height= 2, font=("Arial", 13),
	command= lambda : vh_selected(0, root,lista_Vh, vhs, lis_Wid_2), bg= "#0088b6")
	tren.grid(row= 1, column= 0)

	avion = Button(root, text= "Avion", width= 30, height= 2, font=("Arial", 13),
	command= lambda : vh_selected(1, root,lista_Vh, vhs, lis_Wid_2), bg= "#0088b6")
	avion.grid(row= 1, column= 1)

	camion = Button(root, text= "Camion", width= 30, height= 2, font=("Arial", 13),
	command= lambda : vh_selected(2, root,lista_Vh, vhs, lis_Wid_2), bg= "#0088b6")
	camion.grid(row= 1, column= 2)

	lis_Wid_2 = [lbl_sel, tren, avion, camion]

#========================================================================#
#====== Mostrar Cantidad de vehiculos para el tipo seleccionado =========#
#========================================================================#

def vh_selected(index, root, lista_Vh, vhs, lis_Wid_2):
	cant_Vh = len(lista_Vh[index])
	var_Response = IntVar()
	lbl_quest = Label(root, font=("Arial", 13), bg= "#0088b6",
	text= f"Hay {cant_Vh} {vhs[index]}\nQue numero de vehiculo deseas elegir: "
	, justify= CENTER)
	lbl_quest.grid(row= 2, column= 1)
	lis_Wid_2.append(lbl_quest)
	
	response = Entry(root, font=("Arial", 13), bg= "#0088b6", textvariable= var_Response)
	response.grid(row= 3, column= 1)
	lis_Wid_2.append(response)

	but_get = Button(root, text= "Obtener datos del vehiculo", font=("Arial", 13),
	command= lambda : print_Vh(root,
														index,
														var_Response.get(),
														lista_Vh,
														lis_Wid_2), bg= "#0088b6")
	but_get.grid(row= 4, column= 1)
	lis_Wid_2.append(but_get)

def print_Vh(root, index, index_2, lista_Vh, lis_Wid_2):
	clean_wid(lis_Wid_2)
	vh = lista_Vh[index][index_2 - 1]

	vh.punto_3_1(root)
	vh.punto_3_2(root)
	vh.punto_3_3(root)
	vh.punto_3_4(root)
	vh.punto_3_5(root)

#========================================================================#
#================ indice 4.1 :Costo total de transporte =================#
#========================================================================#

def indice_4_1(root, lis_Wid, lista_Vh,):
	clean_wid(lis_Wid)
	total_Transporte = 0
	for x in range(len(lista_Vh)):
		for y in range(len(lista_Vh[x])):
			total_Transporte += lista_Vh[x][y].costo
	lbl_text = Label(root, font=("Arial", 13), bg= "#0088b6",
										text=  	f"El costo total de transporte es :"
														f"{total_Transporte}")
	lbl_text.pack()

#========================================================================#
#============= indice 4.2 :Costo total por tipo de transporte ===========#
#========================================================================#

def indice_4_2(root, lista_Vh, vhs):
	l_Total_Por_Tipo_Vh = [0, 0, 0]
	for x in range(len(lista_Vh)):
		for y in range(len(lista_Vh[x])):
			l_Total_Por_Tipo_Vh[x] += lista_Vh[x][y].costo
	for x in range(len(l_Total_Por_Tipo_Vh)):
		lbl_text = Label(root, font=("Arial", 13), bg= "#0088b6",
											text=	f"El costo total por {vhs[x]} es :"
														f" {l_Total_Por_Tipo_Vh[x]}")
		lbl_text.pack()

#========================================================================#
#====================== Limpiar ventana de Widgets ======================#
#========================================================================#

def clean_wid(lis_Wid):
	for x in range(len(lis_Wid)):
		lis_Wid[x].destroy()

#========================================================================#
#=================== Inicialización de funciones ========================#
#========================================================================#

if __name__ == "__main__":
	lista = read_csv("MOCK_DATA.csv")
	lista_Contenedores(lista, lista_Cont)
	cant_Vhs = cant_Vh(cont_Totales(lista_Cont)[0])
	Dep_en_Vh(cant_Vhs, cont_Totales(lista_Cont)[1], lista_Vh)
	root = init_tk()
	inter_form_1(root, lis_Form_1, lista_Vh, vhs)
	root.mainloop()