import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class servicio:
    def __init__(self, root, db):
        self.db = db
        self.data = []
        self.ancho = 600
        self.alto = 400
        self.__ancho = self.ancho / 10
        self.__alto = self.alto / 10

        # Toplevel es una ventana que está un nivel arriba que la principal
        self.root = tk.Toplevel()
        self.root.geometry('%dx%d' % (self.ancho, self.alto))
        self.root.title("Servicio")
        self.root.resizable(width=0, height=0)

        # toplevel modal
        self.root.transient(root)

        # llama a los botones
        self.__config_buttons()

    def __config_buttons(self):
        tk.Button(self.root, text="Ingresar",
                  command=self.__insertar).place(x=2 * self.__ancho, y=1 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)
        tk.Button(self.root, text="Buscar",
                  command=self.__insertar).place(x=6 * self.__ancho, y=1 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)
        tk.Button(self.root, text="Eliminar",
                  command=self.__insertar).place(x=2 * self.__ancho, y=4 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)
        tk.Button(self.root, text="Ver Todo",
                  command=self.__mostrar).place(x=6 * self.__ancho, y=4 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)
        tk.Button(self.root, text="Volver Atrás",
                  command=self.__insertar).place(x=4 * self.__ancho, y=7 * self.__alto, width=2 * self.__ancho,
                                                 height=2 * self.__alto)

    def __insertar(self):
        insertar(self.db, self)

    def __mostrar(self):
        servicios_realizados(self.db, self)


    def __modificar(self):
        if (self.treeview.focus() != ""):  # id, nombre, especie, dueño, descripcion, fecha
            sql = """select mascota.id_mascota, mascota.nom_masc, especie.nom_esp, concat( dueno.nom_due,' ', 
            dueno.ape_due) as nombre , mascota.descrip_masc, date_format(mascota.fecha_nacimiento, "%Y-%m-%d")
            from mascota join dueno on mascota.id_dueno = dueno.id_dueno
            join especie  on mascota.id_especie = especie.id_especie where mascota.id_mascota = %(id_mascota)s;"""

    def __eliminar(self):
        sql = "delete from mascota where id_mascota = %(id_mascota)s"


class insertar:
    def __init__(self, db, padre):
        self.padre = padre
        self.db = db
        self.insert_datos = tk.Toplevel()
        self.__config_window()
        self.__config_label()
        self.__config_entry()
        #self.__checkBotton()
        self.__config_button()

    def __config_window(self):
        self.insert_datos.geometry('500x600')
        self.insert_datos.title("Insertar Mascota")
        self.insert_datos.resizable(width=0, height=0)

    def __config_label(self):  # id, nombre, especie, dueño, descripcion, fecha

        padx = 2
        pady = 5

        self.insert_datos.grid_columnconfigure(10, minsize=100)

        tk.Label(self.insert_datos, text="DATOS MASCOTA", font=("helvetica 9 bold")).grid(row=0, column=0, padx=padx,
                                                                                          pady=pady, columnspan=2,
                                                                                          sticky="NW")
        tk.Label(self.insert_datos, text="  Mascota: ").grid(row=1, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="  Peso: ").grid(row=2, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="DIAGNÓSTICO", font=("helvetica 9 bold")).grid(row=3, column=0, padx=padx,
                                                                                        pady=pady, columnspan=2,
                                                                                        sticky="NW")
        tk.Label(self.insert_datos, text="  Nombre: ").grid(row=4, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="  Observaciones: ").grid(row=5, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="MÉDICO", font=("helvetica 9 bold")).grid(row=6, column=0, padx=padx,
                                                                                   pady=pady, columnspan=2, sticky="NW")
        tk.Label(self.insert_datos, text="  Nombre: ").grid(row=7, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="USO DE INSTALACIONES", font=("helvetica 9 bold")).grid(row=8, column=0,
                                                                                                 pady=pady,
                                                                                                 columnspan=2,
                                                                                                 sticky="NW")
        tk.Label(self.insert_datos, text="Tipo de Jaula :").grid(row=10, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Fecha :").grid(row=11, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Cantidad de dias:").grid(row=12, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Tipo de pabelLon:").grid(row=15, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Fecha :").grid(row=16, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Jaula", font="helvetica 9 bold").grid(row=9, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Pabellón", font="helvetica 9 bold").grid(row=13, column=0, padx=padx, pady=pady,
                                                                                sticky="W")

        tk.Label(self.insert_datos, text="\n").grid(row=16, column=0, padx=padx, pady=pady,
                                                    ipady=10)  # row vacio para generar espacio

    def __checkBotton(self):
        self.var_jaula = tk.IntVar()
        self.var_pabellon = tk.IntVar()

        self.chk_jaula = tk.Checkbutton(self.insert_datos, text=' Uso de Jaula', variable=self.var_jaula, onvalue=1)
        self.chk_jaula.grid(row=9, column=0, pady=5, padx=2, sticky="SW")
        self.chk_pabellon = tk.Checkbutton(self.insert_datos, text=' Uso de Jaula', variable=self.var_pabellon, onvalue=1)
        self.chk_pabellon.grid(row=13, column=0, pady=5, padx=2, sticky="SW")

    def __config_entry(self):
        padx = 2
        pady = 2

        self.combo_mascota = ttk.Combobox(self.insert_datos)
        self.combo_mascota.grid(row=1, column=1, ipadx=90, pady=pady, padx=padx, sticky="W")
        self.combo_mascota["values"], self.id_masc = self.__fill_combo_mascota()
        self.entry_peso = tk.Entry(self.insert_datos)
        self.entry_peso.grid(row=2, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_diagnostico = ttk.Combobox(self.insert_datos)
        self.combo_diagnostico.grid(row=4, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_diagnostico["values"], self.id_diag = self.__fill_combo_diagnostico()
        self.entry_observaciones = tk.Entry(self.insert_datos)
        self.entry_observaciones.grid(row=5, column=1, pady=pady, padx=padx, ipadx=90, sticky="W")
        self.combo_medico = ttk.Combobox(self.insert_datos)
        self.combo_medico.grid(row=7, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_medico["values"], self.id_med = self.__fill_combo_medico()
        self.combo_jaula = ttk.Combobox(self.insert_datos)
        self.combo_jaula.grid(row=10, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_jaula["values"], self.id_jau = self.__fill_combo_jaula()
        self.entry_jaula_fecha = tk.Entry(self.insert_datos)
        self.entry_jaula_fecha.grid(row=11, column=1, pady=pady, padx=padx, sticky="W")
        self.entry_jaula_dias = tk.Entry(self.insert_datos)
        self.entry_jaula_dias.grid(row=12, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_pabellon = ttk.Combobox(self.insert_datos)
        self.combo_pabellon.grid(row=15, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_pabellon["values"], self.id_pab = self.__fill_combo_pabellon()
        self.entry_pabellon_fecha = tk.Entry(self.insert_datos)
        self.entry_pabellon_fecha.grid(row=16, column=1, pady=pady, padx=padx, sticky="W")

    def __config_button(self):
        pady = 2
        padx = 5

        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).grid(row=18, column=1, padx=padx, pady=pady, sticky="W")

    def __insertar(self):  # Insercion en la base de datos.
        vacio1 = ""  # variable para verificar que los tk.Entry no están vacíos
        vacio2 = -1  # variable para verificar que los tk.combobox no están vacíos
        if self.combo_mascota.current() == vacio2:
            self.__popup_error("Se debe seleccionar una mascota ")
        elif self.entry_peso.get() == vacio1:
            self.__popup_error("Se debe ingresar el peso de la mascota")
        elif self.combo_diagnostico.current() == vacio2:
            self.__popup_error("Se debe seleccionar un diagnóstico ")
        elif self.entry_observaciones.get() == vacio1:
            self.__popup_error("Se debe ingresar observaciones ")
        elif self.combo_medico.current() == vacio2:
            self.__popup_error("Se debe seleccionar un diagnóstico ")

        else:
            sql_ser = """insert into servicio(hora, id_mascota, peso) VALUES (now(), %(id_mas)s, %(peso)s) """
            self.db.run_sql(sql_ser, {"id_mas": self.id_masc[self.combo_mascota.current()],
                                      "peso": self.entry_peso.get()})


            sql_realiza = """call pr_insert_realizado(%(id_med)s, %(id_diag)s, %(obs)s) """
            captura = self.db.run_sql(sql_realiza, {"id_med": self.id_med[self.combo_medico.current()],
                                                     "id_diag": self.id_diag[self.combo_diagnostico.current()],
                                                     "obs": self.entry_observaciones.get()})


            self.__popup_ingreso()





            self.insert_datos.destroy()
    def __popup_error(self, error):
        tk.messagebox.showerror("Error al ingresar datos", error)

    def __popup_ingreso(self, ):

        tk.messagebox.showinfo("Aviso", "Datos ingresados exitosamente")


    def __fill_combo_mascota(self):
        sql = "select m.id_mascota, concat(' ',m.nom_masc,',      Dueño: ', nom_due, ' ', ape_due) from mascota m " \
              "join dueno d on m.id_dueno = d.id_dueno;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_medico(self):
        sql = "select id_medico, concat(nom_med, ' ' , ape_med) as nombre from medico;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_diagnostico(self):
        sql = "select id_diag, nom_diag from diagnostico;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_jaula(self):
        sql = "select id_jaula, descripcion from jaula;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_pabellon(self):
        sql = "select id_pabellon, descripcion from pabellon;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]


class servicios_realizados:
    def __init__(self, db, padre):
        self.db = db
        self.padre = padre
        self.data = []

        # Toplevel es una ventana que está un nivel arriba que la principal
        self.padre = tk.Toplevel()
        self.padre.geometry('1520x400')
        self.padre.title("Servicios realizados")
        self.padre.resizable(width=0, height=0)

        # toplevel modal
       # self.padre.transient(root)

        #
        self.__config_treeview()
        self.__config_buttons()

    def __config_treeview(self):
        self.treeview = ttk.Treeview(self.padre)
        self.treeview.configure(columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"))
        self.treeview.heading("#0", text="Id")
        self.treeview.heading("#1", text="Nombre")
        self.treeview.heading("#2", text="Peso (kg)")
        self.treeview.heading("#3", text="Diagnostico")
        self.treeview.heading("#4", text="Observaciones")
        self.treeview.heading("#5", text="Medico")
        self.treeview.heading("#6", text="Fecha")
        self.treeview.heading("#7", text="Jaula")
        self.treeview.heading("#8", text="Pabellón")
        self.treeview.column("#0", minwidth=50, width=50, stretch=False)
        self.treeview.column("#1", minwidth=200, width=200, stretch=False)
        self.treeview.column("#2", minwidth=80, width=80, stretch=False)
        self.treeview.column("#3", minwidth=100, width=200, stretch=False)
        self.treeview.column("#4", minwidth=100, width=200, stretch=False)
        self.treeview.column("#5", minwidth=200, width=200, stretch=False)
        self.treeview.column("#6", minwidth=150, width=150, stretch=False)
        self.treeview.column("#7", minwidth=200, width=200, stretch=False)
        self.treeview.column("#8", minwidth=200, width=200, stretch=False)
        self.treeview.place(x=0, y=0, height=350, width=1599)
        self.llenar_treeview()
        self.padre.after(0, self.llenar_treeview)

    def __config_buttons(self):
        tk.Button(self.padre, text="Modificar Servicio",
                  command=self.__modificar).place(x=200, y=350, width=200, height=50)
        tk.Button(self.padre, text="Eliminar Servicio",
                  command=self.__eliminar).place(x=400, y=350, width=200, height=50)

    # select  a la base de datos para obtener id, nombre, apellido, fecha ingreso del medico
    def llenar_treeview(self):
        sql = """select * from vista_servicio;"""
        # obtiene los datos
        data = self.db.run_select(sql)

        if (data != self.data):
            self.treeview.delete(*self.treeview.get_children())  # Elimina todos los rows del treeview
            for i in data:
                self.treeview.insert("", "end", text=i[0],
                                     values=(i[1].replace(" ", "\\ ") + " " + i[2] + " " + i[3].replace(" ", "\\ ") +
                                             " " + i[4].replace(" ", "\\ ") + " " + i[5].replace(" ", "\\ ") + " " +
                                             i[6].replace(" ", "\\ ") + " " + i[7].replace(" ", "\\ ") + " " + i[8].replace(" ", "\\ "))
                                     , iid=i[0], tags="rojo")

            self.data = data

    def __modificar(self):
        if (self.treeview.focus() != ""): #id, nombre, especie, dueño, descripcion, fecha
            sql = """select * from modi_servicio where id_servicio = %(id_servicio)s;"""

            row_data = self.db.run_select_filter(sql, {"id_servicio": self.treeview.focus()})[0]
            modificar(self.db, self, row_data)

    def __eliminar(self):
        sql = "delete from mascota where id_mascota = %(id_mascota)s"
        self.db.run_sql(sql, {"id_mascota": self.treeview.focus()})
        self.llenar_treeview()


class modificar:
    def __init__(self, db, padre, row_data):
        self.padre = padre
        self.db = db
        self.row_data = row_data
        self.insert_datos = tk.Toplevel()
        self.__config_window()
        self.__config_label()
        self.__config_entry()
        self.__config_button()

    def __config_window(self):
        self.insert_datos.geometry('500x600')
        self.insert_datos.title("Modificar Servicio")
        self.insert_datos.resizable(width=0, height=0)

    def __config_label(self):  # id, nombre, especie, dueño, descripcion, fecha

        padx = 2
        pady = 5

        self.insert_datos.grid_columnconfigure(10, minsize=100)

        tk.Label(self.insert_datos, text="DATOS MASCOTA", font=("helvetica 9 bold")).grid(row=0, column=0, padx=padx,
                                                                                          pady=pady, columnspan=2,
                                                                                          sticky="NW")
        tk.Label(self.insert_datos, text="  Mascota: ").grid(row=1, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="  Peso: ").grid(row=2, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="DIAGNÓSTICO", font=("helvetica 9 bold")).grid(row=3, column=0, padx=padx,
                                                                                        pady=pady, columnspan=2,
                                                                                        sticky="NW")
        tk.Label(self.insert_datos, text="  Nombre: ").grid(row=4, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="  Observaciones: ").grid(row=5, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="MÉDICO", font=("helvetica 9 bold")).grid(row=6, column=0, padx=padx,
                                                                                   pady=pady, columnspan=2, sticky="NW")
        tk.Label(self.insert_datos, text="  Nombre: ").grid(row=7, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="USO DE INSTALACIONES", font=("helvetica 9 bold")).grid(row=8, column=0,
                                                                                                 pady=pady,
                                                                                                 columnspan=2,
                                                                                                 sticky="NW")
        tk.Label(self.insert_datos, text="Tipo de Jaula :").grid(row=10, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Fecha :").grid(row=11, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Cantidad de dias:").grid(row=12, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Tipo de pabelLon:").grid(row=15, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Fecha :").grid(row=16, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Jaula", font="helvetica 9 bold").grid(row=9, column=0, padx=padx, pady=pady,
                                                                                sticky="W")
        tk.Label(self.insert_datos, text="Pabellón", font="helvetica 9 bold").grid(row=13, column=0, padx=padx,
                                                                                   pady=pady,
                                                                                   sticky="W")

        tk.Label(self.insert_datos, text="\n").grid(row=16, column=0, padx=padx, pady=pady,
                                                    ipady=10)  # row vacio para generar espacio

    def __checkBotton(self):
        self.var_jaula = tk.IntVar()
        self.var_pabellon = tk.IntVar()

        self.chk_jaula = tk.Checkbutton(self.insert_datos, text=' Uso de Jaula', variable=self.var_jaula, onvalue=1)
        self.chk_jaula.grid(row=9, column=0, pady=5, padx=2, sticky="SW")
        self.chk_pabellon = tk.Checkbutton(self.insert_datos, text=' Uso de Jaula', variable=self.var_pabellon,
                                           onvalue=1)
        self.chk_pabellon.grid(row=13, column=0, pady=5, padx=2, sticky="SW")

    def __config_entry(self):
        padx = 2
        pady = 2

        self.combo_mascota = ttk.Combobox(self.insert_datos)
        self.combo_mascota.grid(row=1, column=1, ipadx=90, pady=pady, padx=padx, sticky="W")
        self.combo_mascota["values"], self.id_masc = self.__fill_combo_mascota()
        self.combo_mascota.insert(0, self.row_data[1])
        self.entry_peso = tk.Entry(self.insert_datos)
        self.entry_peso.grid(row=2, column=1, pady=pady, padx=padx, sticky="W")
        self.entry_peso.insert(0, self.row_data[2])
        self.combo_diagnostico = ttk.Combobox(self.insert_datos)
        self.combo_diagnostico.grid(row=4, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_diagnostico["values"], self.id_diag = self.__fill_combo_diagnostico()
        self.combo_diagnostico.insert(0, self.row_data[3])
        self.entry_observaciones = tk.Entry(self.insert_datos)
        self.entry_observaciones.grid(row=5, column=1, pady=pady, padx=padx, ipadx=90, sticky="W")
        self.entry_observaciones.insert(0, self.row_data[4])
        self.combo_medico = ttk.Combobox(self.insert_datos)
        self.combo_medico.grid(row=7, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_medico["values"], self.id_med = self.__fill_combo_medico()
        self.combo_medico.insert(0, self.row_data[5])
        self.combo_jaula = ttk.Combobox(self.insert_datos)
        self.combo_jaula.grid(row=10, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_jaula["values"], self.id_jau = self.__fill_combo_jaula()
        #self.combo_jaula.insert(0, self.row_data[5])
        self.entry_jaula_fecha = tk.Entry(self.insert_datos)
        self.entry_jaula_fecha.grid(row=11, column=1, pady=pady, padx=padx, sticky="W")
        self.entry_jaula_fecha.insert(0, self.row_data[6])
        self.entry_jaula_dias = tk.Entry(self.insert_datos)
        self.entry_jaula_dias.grid(row=12, column=1, pady=pady, padx=padx, sticky="W")
        #self.entry_jaula_dias.insert(0, self.row_data[7])
        self.combo_pabellon = ttk.Combobox(self.insert_datos)
        self.combo_pabellon.grid(row=15, column=1, pady=pady, padx=padx, sticky="W")
        self.combo_pabellon["values"], self.id_pab = self.__fill_combo_pabellon()
        #self.combo_pabellon.insert(0, self.row_data[8])
        self.entry_pabellon_fecha = tk.Entry(self.insert_datos)
        self.entry_pabellon_fecha.grid(row=16, column=1, pady=pady, padx=padx, sticky="W")

    def __config_button(self):
        pady = 2
        padx = 5

        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).grid(row=18, column=1, padx=padx, pady=pady, sticky="W")

    def __insertar(self):  # Insercion en la base de datos.
        vacio1 = ""  # variable para verificar que los tk.Entry no están vacíos
        vacio2 = -1  # variable para verificar que los tk.combobox no están vacíos
        if self.combo_mascota.current() == vacio2:
            self.__popup_error("Se debe seleccionar una mascota ")
        elif self.entry_peso.get() == vacio1:
            self.__popup_error("Se debe ingresar el peso de la mascota")
        elif self.combo_diagnostico.current() == vacio2:
            self.__popup_error("Se debe seleccionar un diagnóstico ")
        elif self.entry_observaciones.get() == vacio1:
            self.__popup_error("Se debe ingresar observaciones ")
        elif self.combo_medico.current() == vacio2:
            self.__popup_error("Se debe seleccionar un diagnóstico ")

        else:
            sql_ser = """insert into servicio(hora, id_mascota, peso) VALUES (now(), %(id_mas)s, %(peso)s) """
            self.db.run_sql(sql_ser, {"id_mas": self.id_masc[self.combo_mascota.current()],
                                      "peso": self.entry_peso.get()})

            sql_realiza = """call pr_insert_realizado(%(id_med)s, %(id_diag)s, %(obs)s) """
            captura = self.db.run_sql(sql_realiza, {"id_med": self.id_med[self.combo_medico.current()],
                                                    "id_diag": self.id_diag[self.combo_diagnostico.current()],
                                                    "obs": self.entry_observaciones.get()})

            self.__popup_ingreso()

            self.insert_datos.destroy()

    def __popup_error(self, error):
        tk.messagebox.showerror("Error al ingresar datos", error)

    def __popup_ingreso(self, ):

        tk.messagebox.showinfo("Aviso", "Datos ingresados exitosamente")

    def __fill_combo_mascota(self):
        sql = "select m.id_mascota, concat(' ',m.nom_masc,',      Dueño: ', nom_due, ' ', ape_due) from mascota m " \
              "join dueno d on m.id_dueno = d.id_dueno;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_medico(self):
        sql = "select id_medico, concat(nom_med, ' ' , ape_med) as nombre from medico;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_diagnostico(self):
        sql = "select id_diag, nom_diag from diagnostico;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_jaula(self):
        sql = "select id_jaula, descripcion from jaula;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_pabellon(self):
        sql = "select id_pabellon, descripcion from pabellon;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def modificar(self):  # Insercion en la base de datos.
        sql = """update medico set nom_med = %(nom_med)s, ape_med = %(ape_med)s,
            fecha_ingreso = %(fecha_ingreso)s where id_medico = %(id_medico)s"""
        self.db.run_sql(sql, {"nom_med": self.entry_nombre.get(), "fecha_ingreso": self.entry_fecha.get(),
                              "ape_med": self.entry_apellido.get(), "id_medico": int(self.row_data[0])})
        self.insert_datos.destroy()
        self.padre.llenar_treeview_medico()