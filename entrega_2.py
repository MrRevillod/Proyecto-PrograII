from run import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

TextList = ["Cantidad total de vehículos", "Cantidad total de cada vehículo",
            "Selecciona uno de los vehículos", "Costos totales de transporte"]

# __Funcion_Init_____________________________________________


def Tkinter_Init():
    root = Tk()
    root.title("Proyecto de Programación II - INFO1123")
    root.geometry('1000x600+250+250')
    root['bg'] = 'grey'
    root.resizable(False, False)
    # __ grid layout (4x4) ____________
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    return root

# __Funcion_que_genera_contenedor_principal__________________

# ___Crea_un_contenedor_principal_de_4x4___


def Init_Main_Cont(root):
    main = Frame(root, bg="grey", padx=10, pady=10)
    main.grid(row=0, column=1, sticky="nsew")

    # __Grid_layout_(4x4)_____________

    main.grid_columnconfigure((0, 1, 2, 3), weight=1)
    main.grid_rowconfigure((0, 1, 2, 3), weight=1)

    return main


# __Funcion_que_vacia_el_contenedor_Main__________________

# __Recorre todos los qidgets y elementos hijos del contenedor y los destruye

def Clear_Main_Cont(main):
    for widget in main.winfo_children():
        widget.destroy()
    return

# __Funcion_que_genera_contenedor_Side_Bar__________________

# __Crea_un_contenedor_secundario_de_4x1__


def Create_SideBar(root, main, Vehiculos_Txt, lista_Vh, cant_Vhs):
	sidebar = Frame(root, bg="grey", padx=10, pady=10)
	sidebar.grid(row=0, column=0, sticky="nsew")

	sidebar.grid_rowconfigure((0, 1, 2, 3), weight=1)

	# __Metodo_que_genera_botones_de_SideBar________________

	btn1 = Button(
			sidebar, text="Cant total de vehiculos", command=lambda: Switcher(1, main, Vehiculos_Txt, lista_Vh, cant_Vhs))
	btn1.grid(row=0, column=0, sticky="nsew")

	btn2 = Button(
			sidebar, text="Cant total de cada vehiculo", command=lambda: Switcher(2, main, Vehiculos_Txt, lista_Vh, cant_Vhs))
	btn2.grid(row=1, column=0, sticky="nsew")

	btn3 = Button(
			sidebar, text="Seleccionar un Vehiculo", command=lambda: Switcher(3, main, Vehiculos_Txt, lista_Vh, cant_Vhs))
	btn3.grid(row=2, column=0, sticky="nsew")

	btn4 = Button(
			sidebar, text="Costo total de los vehiculos", command=lambda: Switcher(4, main, Vehiculos_Txt, lista_Vh, cant_Vhs))
	btn4.grid(row=3, column=0, sticky="nsew")

	return


# __Funcion_Switcher__________________________________________

def Switcher(option, main, Vehiculos_Txt, lista_Vh, cant_Vhs):

    if option == 1:
        Enunciado_I(main, lista_Vh)
    elif option == 2:
        Enunciado_II(main, lista_Vh)
    elif option == 3:
        Enunciado_III(main, lista_Vh, Vehiculos_Txt)
    elif option == 4:
        Enunciado_IV_I(main, lista_Vh, cant_Vhs)
        Enunciado_IV_II(main, lista_Vh, cant_Vhs, Vehiculos_Txt)
    return

# __Funcion_que_genera_Enunciado_I____________________________

# __Debe recibir un numero X entero que represente la cantidad total de vehiculos


def Enunciado_I(main, lista_Vh):

	total_vehiculos = float(0)
	for x in range(len(lista_Vh)):
			total_vehiculos += len(lista_Vh[x])

	Clear_Main_Cont(main)

	Frame1 = Frame(main)
	Frame1.grid(row=0, column=0, rowspan=2, columnspan=4)

	Text1 = Label(Frame1, text="La cantidad total de Vehiculos es:", font=("Arial", 15), bg="grey")
	Text1.grid(sticky="n")

	Frame2 = Frame(main)
	Frame2.grid(row=2, column=0, rowspan=2, columnspan=4)

	Text2 = Label(Frame2, text=int(total_vehiculos), font=("Arial", 30), bg="grey")
	Text2.grid(sticky="n")

	return

# __Funcion_que_genera_Enunciado_II____________________________

def Enunciado_II(main, lista_Vh):

	Clear_Main_Cont(main)

	# img1 = Image.open("./img/barco.png"); img2 = Image.open("./img/tren.png")
	# img3 = Image.open("./img/avion.png"); img4 = Image.open("./img/camion.png")

	# imgB = ImageTk.PhotoImage(img1) ; imgT = ImageTk.PhotoImage(img2)
	# imgA = ImageTk.PhotoImage(img3) ; imgC = ImageTk.PhotoImage(img4)
	# imgB = PhotoImage(file=r"C:\xampp\htdocs\Proyecto-PrograII\img\barco.png")
	# imgT = PhotoImage(file=r"C:\xampp\htdocs\Proyecto-PrograII\img\tren.png")
	# imgA = PhotoImage(file=r"C:\xampp\htdocs\Proyecto-PrograII\img\avion.png")
	# imgC = PhotoImage(file=r"C:\xampp\htdocs\Proyecto-PrograII\img\camion.png")
	# listaImg = [imgB, imgT, imgA, imgC]

	total_Por_Vh = []
	for x in range(len(lista_Vh)):
		total_Por_Vh.append(len(lista_Vh[x]))

	lis_strings = [
		"La cantidad total de barcos es: "  , "La cantidad total de trenes es: ",
		"La cantidad total de aviones es: " , "La cantidad total de camiones es: "
		]
	for x in range(len(lista_Vh)):
		Texto = Label(main, text = (lis_strings[x] + str(total_Por_Vh[x])), font=("Arial", 11), bg="grey", borderwidth= 4)
		Texto.grid(row=x, column=0)

	# Img = Label(main, image=imgB)
	# Img.grid(row=0, column=1)

	# for x in range(len(listaImg)):
	# 	Img = Label(main, image=listaImg[x])
	# 	Img.grid(row=x, column=1)


# __Funcion_que_genera_Enunciado_III____________________________

def Enunciado_III(main, lista_Vh, Vh_strings):

	Clear_Main_Cont(main)

	# __Metodo_que_genera_EL_TITULO_de_Enunciado_III____________

	Label_III = Label(main, text="Seleccionar un tipo de vehiculo", font=("Arial", 15), bg="grey",
										width=50, height=0)
	Label_III.grid(row=0, column=1, columnspan=2, sticky="nsew")

	# __Metodo_que_genera_4_BOTONES___________

	Label_btns = Label(main, bg="grey", width=100,
										height=10, background="black")
	Label_btns.grid(row=1, column=1, columnspan=2, sticky="n")

	envInt = IntVar()

	Barco = Button(
		Label_btns, text="Barco", width=15, height=2
		, command=lambda : Enunciado_III_Input(0, main, lista_Vh, Vh_strings))
	Barco.grid(row=1, column=0, rowspan=1, sticky="new")

	Tren = Button(
		Label_btns, text="Tren", width=15, height=2
		, command=lambda : Enunciado_III_Input(1, main, lista_Vh, Vh_strings))
	Tren.grid(row=1, column=1, rowspan=1, sticky="new")

	Avion = Button(
		Label_btns, text="Avion", width=15, height=2
		, command=lambda : Enunciado_III_Input(2, main, lista_Vh, Vh_strings))
	Avion.grid(row=1, column=2, rowspan=1, sticky="new")

	Camion = Button(
		Label_btns, text="Camion", width=15, height=2
		, command=lambda : Enunciado_III_Input(3, main, lista_Vh, Vh_strings))
	Camion.grid(row=1, column=3, rowspan=1, sticky="new")

def Enunciado_III_Input(num, main, lista_Vh, Vh_strings):

	lis_widgets = main.winfo_children()
	if len(lis_widgets) >=3:
		lis_widgets[-1].destroy()

	frameEntry = Frame(main, bg="grey")
	frameEntry.grid_columnconfigure((0, 1),  weight=1)
	frameEntry.grid_rowconfigure((0, 1, 2), weight=1)
	frameEntry.grid(row=2, column=1, columnspan=2)

	Label_txt = Label(frameEntry, font=("Arial", 11), bg="grey", justify=CENTER,
										text=f"Existen {len(lista_Vh[num])} {Vh_strings[num]} elige 1:")
	Label_txt.grid(row=0, column=0, pady=15,  sticky="nsew")

	envInt = IntVar()

	Input_Box = Entry(frameEntry, justify=CENTER, textvariable=envInt)
	Input_Box.grid(row=1, column=0, pady=15, sticky="nsew")

	enviar = Button(frameEntry, text= "Enviar", justify=CENTER,
									command=lambda : Respuesta_Enun_III(main, num, envInt.get() - 1))
	enviar.grid(row=2, column=0, pady=15, sticky="nsew")

	# __Funcion_que_genera_Enunciado_IV_I____________________________

def Respuesta_Enun_III(main, index, id_Vh):

	Clear_Main_Cont(main)

	lista_Vh[index][id_Vh].punto_3_1(main)
	lista_Vh[index][id_Vh].punto_3_2(main)
	lista_Vh[index][id_Vh].punto_3_3(main)
	lista_Vh[index][id_Vh].punto_3_4(main)
	lista_Vh[index][id_Vh].punto_3_5(main)


def Enunciado_IV_I(main, lista_Vh, cant_Vhs):

	Clear_Main_Cont(main)

	main.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
	main.grid_columnconfigure((0, 1, 2, 3), weight=1)

	precio_total = 0
	for x in range(len(lista_Vh)):
		precio_total += (len(lista_Vh[x]) * cant_Vhs[x][1])

	print(f"El precio total de el transporte de todos los contenedores es: {precio_total}")

	Label_IV = Label(main, text=f"El costo total corresponde a {precio_total}", font=("Arial", 13), bg="grey")
	Label_IV.grid(row=0, column=1, columnspan=2, sticky="nsew")

# __Funcion_que_genera_Enunciado_IV_II____________________________


def Enunciado_IV_II(main, lista_Vh, cant_Vhs, Vehiculos_Txt):

	Clear_Main_Cont(main)

	lis_Precios_Por_Vh = [0, 0, 0, 0]
	for x in range(len(lista_Vh)):
		lis_Precios_Por_Vh[x] += (len(lista_Vh[x]) * cant_Vhs[x][1])
		Label_enunciados = Label(main, bg="grey", font=("Arial", 13),
															text=f"El precio para los {Vehiculos_Txt[x]} es : {lis_Precios_Por_Vh[x]}")
		Label_enunciados.grid(row=x+1, column=1, columnspan=2, sticky="nsew")

# __Ejecucion_Principal________________________________________

Pbarco = 1000000000 ; Ptren = 10000000 ; Pavion = 1000000 ; Pcamion = 500000

if __name__ == "__main__":

	insert_to_db(read_csv("MOCK_DATA_Eval_4.csv"))
	lista = get_list_to_db()
	# lista = read_csv("MOCK_DATA_Eval_4.csv")
	run_Lis_Cont(lista, lis_Cont_N, lis_Cont_R, lis_Cont_I)
	cantidad_Total, lista_All_Dep = run_Cont_Total(lis_Cont_N, lis_Cont_R, lis_Cont_I)
	cant_Vhs = cant_Vh(cantidad_Total, Pbarco, Ptren, Pavion, Pcamion)
	Dep_en_Vh(cant_Vhs[0][0], 24000, 0, cant_Vhs,  lista_All_Dep, lista_Vh)
	Dep_en_Vh(cant_Vhs[1][0], 250,   1, cant_Vhs,  lista_All_Dep, lista_Vh)
	Dep_en_Vh(cant_Vhs[2][0], 10,    2, cant_Vhs,  lista_All_Dep, lista_Vh)
	Dep_en_Vh(cant_Vhs[3][0], 1,     3, cant_Vhs,  lista_All_Dep, lista_Vh)

	Vehiculos_Txt = ["Barcos", "Trenes", "Aviones", "Camiones"]

	root = Tkinter_Init()
	main = Init_Main_Cont(root)

	Create_SideBar(root, main, Vehiculos_Txt, lista_Vh, cant_Vhs)
	root.mainloop()