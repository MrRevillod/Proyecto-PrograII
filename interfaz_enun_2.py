import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # __Window____________________

        self.title("Proyecto Semestral")
        self.resizable(False, False)
        self.geometry(f"{1100}x{580}")

        # grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # __Widgets____________________

        self.sidebar = tk.Frame(self, bg="grey", padx=10, pady=10)
        self.sidebar.grid(row=0, column=0, rowspan=3, sticky="ns")

        self.sidebar.grid_columnconfigure(0, weight=1)
        self.sidebar.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.btn1 = tk.Button(
            self.sidebar, text="Cant total de vehículos", padx=10, pady=10)
        self.btn1.grid(row=0, column=0, sticky="nsew")

        self.btn2 = tk.Button(
            self.sidebar, text="Cant total de cada vehículo", padx=10, pady=10)
        self.btn2.grid(row=1, column=0, sticky="nsew")

        self.btn3 = tk.Button(
            self.sidebar, text="Seleccionar un Vehiculo", padx=10, pady=10)
        self.btn3.grid(row=2, column=0, sticky="nsew")

        self.btn4 = tk.Button(
            self.sidebar, text="Costo total de los vehículos", padx=10, pady=10)
        self.btn4.grid(row=3, column=0, sticky="nsew")

        self.btn1.config(
            bg="white",
            fg="black",
            font=("Arial", 12),
            relief="flat",
            activebackground="grey",
            activeforeground="white",
            borderwidth=10,
            border=10,
            command=lambda: Enunciado_I()
        )

        self.btn2.config(
            bg="white",
            fg="black",
            font=("Arial", 12),
            relief="flat",
            activebackground="grey",
            activeforeground="white",
            command=lambda: Enunciado_II()
        )

        self.btn3.config(
            bg="white",
            fg="black",
            font=("Arial", 12),
            relief="flat",
            activebackground="grey",
            activeforeground="white",
            command=lambda: Enunciado_III()
        )

        self.btn4.config(
            bg="white",
            fg="black",
            font=("Arial", 12),
            relief="flat",
            activebackground="grey",
            activeforeground="white",
        )

        def Enunciado_I():

            self.frame = tk.Label(
                self, bg="grey", padx=50, pady=50, text="Cantidad total de vehículos: 100", font=("Arial", 13))
            self.frame.grid(row=0, column=1, rowspan=3, sticky="nsew")

            self.frame.grid_columnconfigure((0), weight=1)
            self.frame.grid_rowconfigure((0), weight=1)

        def Enunciado_II():

            self.frame = tk.Label(self, bg="grey", padx=10, pady=10)
            self.frame.grid(row=0, column=1, rowspan=3, sticky="nsew")

            self.frame.grid_columnconfigure((0, 1), weight=1)
            self.frame.grid_rowconfigure((0, 1), weight=1)

            img_tren = tk.PhotoImage(file=r"./img/tren.png")

            self.cont1 = tk.Label(
                self.frame, bg="grey", padx=10, pady=10, text=f"Cantidad de Aviones:",)
            self.cont1.grid(row=0, column=0, sticky="nsew")

            self.cont2 = tk.Label(self.frame, bg="white",
                                  padx=10, pady=10, text=f"Cantidad de Camiones:")
            self.cont2.grid(row=0, column=1, sticky="nsew")

            self.cont3 = tk.Label(self.frame, bg="white",
                                  padx=10, pady=10, text=f"Cantidad de Barcos:")
            self.cont3.grid(row=1, column=0, sticky="nsew")

            self.cont4 = tk.Label(
                self.frame, bg="grey", padx=10, pady=10, text=f"Cantidad de Trenes:")
            self.cont4.grid(row=1, column=1, sticky="nsew")

        def Enunciado_III():

            self.frame_top = tk.Label(self, bg="grey", padx=10, pady=0,
                                      text="Seleccionar un vehículo", font=("Arial", 13))
            self.frame_top.grid(row=0, column=1, sticky="nsew")

            self.frame = tk.Label(self, bg="grey", padx=10, pady=20)
            self.frame.grid(row=1, column=1, rowspan=1, sticky="nsew")

            self.frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

            self.btn5 = tk.Button(
                self.frame, text="Avión", padx=10, pady=10)
            self.btn5.grid(row=0, column=0, sticky="nsew")

            self.btn6 = tk.Button(
                self.frame, text="Camión", padx=10, pady=10)
            self.btn6.grid(row=0, column=1, sticky="nsew")

            self.btn7 = tk.Button(
                self.frame, text="Barco", padx=10, pady=10)
            self.btn7.grid(row=0, column=2, sticky="nsew")

            self.btn8 = tk.Button(
                self.frame, text="Tren", padx=10, pady=10)
            self.btn8.grid(row=0, column=3, sticky="nsew")

            self.btn5.config(
                bg="white",
                fg="black",
                font=("Arial", 12),
                relief="flat",
                activebackground="grey",
                activeforeground="white",
                borderwidth=10,
                border=10,
                command=lambda: Enunciado_III_I()
            )

            self.btn6.config(
                bg="white",
                fg="black",
                font=("Arial", 12),
                relief="flat",
                activebackground="grey",
                activeforeground="white",
            )

            self.btn7.config(
                bg="white",
                fg="black",
                font=("Arial", 12),
                relief="flat",
                activebackground="grey",
                activeforeground="white",
            )

            self.btn8.config(
                bg="white",
                fg="black",
                font=("Arial", 12),
                relief="flat",
                activebackground="grey",
                activeforeground="white",
            )

        def Enunciado_III_I():
            # add a new label with entry

            self.label_entry = tk.Label(
                self.frame, bg="grey", padx=10, pady=10, text="Ingresa el numero de Avion:", font=("Arial", 13))
            self.label_entry.grid(row=2, column=1, rowspan=2, sticky="nsew")

            self.entry = tk.Entry(self.frame, bg="white")
            self.entry.grid(row=4, column=1, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
