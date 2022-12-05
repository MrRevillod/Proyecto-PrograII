from kernel import *
from tkinter import *


TextList = ["Cantidad total de vehículos", "Cantidad total de cada vehículo",
            "Selecciona uno de los vehículos", "Costos totales de transporte"]

Trans_Names = ["trenes", "aviones", "camiones", "barcos"]

# __Funcion_Init_____________________________________________


def Tkinter_Init():
    root = Tk()
    root.title("Proyecto de Programación II - INFO1123")
    root.geometry('1000x600+250+250')
    root['bg'] = 'grey'
    root.resizable(False, False)

    # __ grid layout (4x4) ____________
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure((0, 1, 2), weight=1)
    return root

# __Funcion_que_genera_contenedor_principal__________________

# ___Crea_un_contenedor_principal_de_4x4___


def Init_Main_Cont(root):
    main = Frame(root, bg="grey", padx=10, pady=10)
    main.grid(row=0, column=1, rowspan=3, sticky="nsew")

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


def Create_SideBar(root, main, Vehiculos_Txt):

    sidebar = Frame(root, bg="grey", padx=10, pady=10)
    sidebar.grid(row=0, column=0, rowspan=3, sticky="nsew")

    sidebar.grid_columnconfigure(0, weight=1)
    sidebar.grid_rowconfigure((0, 1, 2, 3), weight=1)

    # __Metodo_que_genera_botones_de_SideBar________________

    btn1 = Button(
        sidebar, text="Cant total de vehículos", padx=10, pady=10, command=lambda: Switcher(1, main, Vehiculos_Txt))
    btn1.grid(row=0, column=0, sticky="nsew")

    btn2 = Button(
        sidebar, text="Cant total de cada vehículo", padx=10, pady=10, command=lambda: Switcher(2, main, Vehiculos_Txt))
    btn2.grid(row=1, column=0, sticky="nsew")

    btn3 = Button(
        sidebar, text="Seleccionar un Vehiculo", padx=10, pady=10, command=lambda: Switcher(3, main, Vehiculos_Txt))
    btn3.grid(row=2, column=0, sticky="nsew")

    btn4 = Button(
        sidebar, text="Costo total de los vehículos", padx=10, pady=10, command=lambda: Switcher(4, main, Vehiculos_Txt))
    btn4.grid(row=3, column=0, sticky="nsew")

    return


# __Funcion_Switcher__________________________________________

def Switcher(option, main, Vehiculos_Txt):

    if option == 1:
        Enunciado_I(main, Vehiculos_Txt)
    elif option == 2:
        Enunciado_II(main, Vehiculos_Txt)
    elif option == 3:
        Enunciado_III(main, Vehiculos_Txt)
    elif option == 4:
        Enunciado_IV_I(main, Vehiculos_Txt)
        #Enunciado_IV_II(main, Vehiculos_Txt)
    return

# __Funcion_que_genera_Enunciado_I____________________________

# __Debe recibir un numero X entero que represente la cantidad total de vehiculos


def Enunciado_I(main, Vehiculos_Txt):

    Clear_Main_Cont(main)
    Create_SideBar(root, main, Vehiculos_Txt)

    #Text = f" La cantidad total de Vehiculos es: {x} "
    Text = " La cantidad total de Vehiculos es:  "

    # __Metodo_que_genera_contenedor_de_Enunciado_I____________

    Label_I = Label(main, text=Text, font=("Arial", 15), bg="grey",
                    padx=5, pady=5, width=50, height=10)
    Label_I.grid(row=0, column=1, columnspan=2, sticky="nsew")

    # __Metodo_que_genera_contenedor_para_imagen____________

    img = PhotoImage(file="./img/vehicles.png")
    Label_img = Label(main, image=img)
    Label_img.grid(row=1, column=1, columnspan=2)

    return


# __Funcion_que_genera_Enunciado_II____________________________

def Enunciado_II(main, Vehiculos_Txt):

    Clear_Main_Cont(main)
    Create_SideBar(root, main, Vehiculos_Txt)

    # reemplazar con lista real que contenga la cantidad de cada vehiculo
    numeros = [0, 0, 0, 0]
    # Vehiculos_Txt = ["Trenes", "Aviones", "Camiones", "Barcos"]

    for i in range(len(numeros)):
        Texto = f"La cantidad de {Vehiculos_Txt[i]} es: {numeros[i]}"

        # __LEFT____________________________________________________

        Label_II = Label(main, text=Texto, font=("Arial", 10),
                         bg="grey", padx=0, pady=50, width=10, height=50, background="white", borderwidth=4, relief="groove", )

        Label_II.grid(row=i, column=0, columnspan=1, sticky="nsew")

        # __MIDD____________________________________________________

        Label_II_arrow = Label(main, text="->", font=("Arial", 20),
                               bg="grey", padx=0, pady=50, width=10, height=50, background="white", borderwidth=4, relief="groove")

        Label_II_arrow.grid(row=i, column=1, columnspan=2, sticky="nsew")

        # __RIGHT____________________________________________________

        Label_II_Img = Label(main, text=Vehiculos_Txt[i], font=("Arial", 10),
                             bg="grey", padx=0, pady=50, width=10, height=50, background="white", borderwidth=4, relief="groove")

        Label_II_Img.grid(row=i, column=3, columnspan=1, sticky="nsew")

# __Funcion_que_genera_Enunciado_III____________________________


def Enunciado_III(main, Vehiculos_Txt):

    Clear_Main_Cont(main)
    Create_SideBar(root, main, Vehiculos_Txt)

    # __Metodo_que_genera_EL_TITULO_de_Enunciado_III____________

    Label_III = Label(main, text="Seleccionar un tipo de vehiculo", font=("Arial", 15), bg="grey",
                      width=50, height=0)
    Label_III.grid(row=0, column=1, columnspan=2, sticky="nsew")

    # __Metodo_que_genera_4_BOTONES___________

    Label_btns = Label(main, bg="grey", width=100,
                       height=10, background="black")
    Label_btns.grid(row=1, column=1, columnspan=2, sticky="n")

    Tren = Button(
        Label_btns, text="Tren", width=15, height=2, borderwidth=2)
    Tren.grid(row=1, column=0, rowspan=1, sticky="new")

    Avion = Button(
        Label_btns, text="Avion", width=15, height=2, borderwidth=2)
    Avion.grid(row=1, column=1, rowspan=1, sticky="new")

    Camion = Button(
        Label_btns, text="Camion", width=15, height=2, borderwidth=2)
    Camion.grid(row=1, column=2, rowspan=1, sticky="new")

    Barco = Button(
        Label_btns, text="Barco", width=15, height=2, borderwidth=2)
    Barco.grid(row=1, column=3, rowspan=1, sticky="new")


def Enunciado_III_Input(main):

    Input_Box = Entry(main, width=50, borderwidth=5)
    Input_Box.grid(row=2, column=1, columnspan=2, sticky="nsew")

    # __Funcion_que_genera_Enunciado_IV_I____________________________


def Enunciado_IV_I(main, Vehiculos_Txt):

    Clear_Main_Cont(main)
    Create_SideBar(root, main, Vehiculos_Txt)

    # __Metodo_que_genera_contenedor_de_Enunciado_I____________

    Label_IV = Label(main, text="El costo total corresponde a: ", font=("Arial", 15), bg="grey",
                     padx=5, pady=5, width=50, height=10)
    Label_IV.grid(row=0, column=1, columnspan=2, sticky="nsew")

# __Funcion_que_genera_Enunciado_IV_II____________________________


def Enunciado_IV_II(main, Vehiculos_Txt):

    Clear_Main_Cont(main)
    Create_SideBar(root, main, Vehiculos_Txt)

 # __Ejecucion_Principal________________________________________


if __name__ == "__main__":

    Vehiculos_Txt = ["Trenes", "Aviones", "Camiones", "Barcos"]

    root = Tkinter_Init()
    main = Init_Main_Cont(root)

    Create_SideBar(root, main, Vehiculos_Txt)
    main.mainloop()
    root.mainloop()
