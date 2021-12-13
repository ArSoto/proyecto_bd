import tkinter as tk
from tkinter import ttk


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
                  command=self.__insertar).place(x=2*self.__ancho, y=1*self.__alto, width=2*self.__ancho, height=2*self.__alto)
        tk.Button(self.root, text="Buscar",
                  command=self.__insertar).place(x=6*self.__ancho, y=1*self.__alto, width=2*self.__ancho, height=2*self.__alto)
        tk.Button(self.root, text="Eliminar",
                  command=self.__insertar).place(x=2*self.__ancho, y=4*self.__alto, width=2*self.__ancho, height=2*self.__alto)
        tk.Button(self.root, text="Ver Todo",
                  command=self.__insertar).place(x=6*self.__ancho, y=4*self.__alto, width=2*self.__ancho, height=2*self.__alto)
        tk.Button(self.root, text="Volver Atrás",
                  command=self.__insertar).place(x=4*self.__ancho, y=7*self.__alto, width=2*self.__ancho, height=2*self.__alto)



    def __insertar(self):
        insertar(self.db, self)

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
        self.__config_button()

    def __config_window(self):
        self.insert_datos.geometry('1200x600')
        self.insert_datos.title("Insertar Mascota")
        self.insert_datos.resizable(width=0, height=0)

        separator = ttk.Separator(self.insert_datos, orient='vertical')
        separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)


    def __config_label(self):#id, nombre, especie, dueño, descripcion, fecha

        padx = 20
        pady = 2

        self.insert_datos.grid_columnconfigure(10, minsize=200)

        tk.Label(self.insert_datos, text="DATOS MASCOTA", font=("helvetica 12 bold")).grid(row=0, column=0, padx=padx,pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t\t").grid(row=0, column=2, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t").grid(row=0, column=3, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t").grid(row=0, column=4, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t").grid(row=0, column=5, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t").grid(row=0, column=6, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t").grid(row=0, column=7, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t").grid(row=0, column=8, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t").grid(row=0, column=9, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="\t").grid(row=0, column=10, padx=padx, pady=pady, sticky="W")

        tk.Label(self.insert_datos, text="  Mascota: ").grid(row=1, column=0, padx=padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="  Peso: ").grid(row=2, column=0, padx=padx, pady=pady, sticky="W")

        tk.Label(self.insert_datos, text="Nombre: ").grid(row=1, column= 5, padx = padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Especie: ").grid(row=2, column=5, padx = padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Dueño: ").grid(row=3, column=5, padx = padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Descripción: ").grid(row=4, column=5, padx = padx, pady=pady, sticky="W")
        tk.Label(self.insert_datos, text="Fecha Nacimiento: ").grid(row=5, column=5, padx = padx, pady=pady, sticky="W")

    def __config_entry(self):

        padx = 10
        pady = 2

        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=160, y=10, width=200, height=20)
        self.combo_mascota = ttk.Combobox(self.insert_datos)
        self.combo_mascota.grid(row=1, column=0, pady=pady, padx=padx)
        self.combo_mascota["values"], self.id_esp = self.__fill_combo_mascota()
        self.combo_dueno = ttk.Combobox(self.insert_datos)
        self.combo_dueno.place(x=160, y=70, width=200, height=20)
        self.combo_dueno["values"], self.id_due = self.__fill_combo_dueno()
        self.entry_descripcion = tk.Entry(self.insert_datos)
        self.entry_descripcion.place(x=160, y=100, width=200, height=20)
        self.entry_fecha= tk.Entry(self.insert_datos)
        self.entry_fecha.place(x=160, y=130, width=200, height=20)

    def __config_button(self):
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.__insertar).place(x=160, y=160, width=200, height=20)

    def __insertar(self):  # Insercion en la base de datos.
        sql = """insert into mascota (nom_masc, id_especie, id_dueno, descrip_masc, fecha_nacimiento ) 
            values (%(nom_mascota)s, %(id_especie)s, %(id_dueno)s, %(descrip_masc)s, %(fecha)s)"""
        self.db.run_sql(sql, {"nom_mascota": self.entry_nombre.get(), "id_especie": self.id_esp[self.combo_mascota.current()],
                              "id_dueno": self.id_due[self.combo_dueno.current()], "descrip_masc": self.entry_descripcion.get(),
                              "fecha": self.entry_fecha.get()})
        self.insert_datos.destroy()
        self.padre.llenar_treeview()

    def __fill_combo_mascota(self):
        sql = "select m.id_mascota, concat(m.nom_masc,', Dueño: ', nom_due, ' ', ape_due) from mascota m " \
              "join dueno d on m.id_dueno = d.id_dueno;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_dueno(self):
        sql = "select id_dueno, concat(dueno.nom_due, ' ' , dueno.ape_due) as nombre from dueno;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]


class modificar:
    def __init__(self, db, padre, row_data):
        self.padre = padre
        self.db = db
        self.row_data = row_data
        self.insert_datos = tk.Toplevel()
        self.config_window()
        self.config_label()
        self.config_entry()
        self.config_button()

    def config_window(self):  # Settings
        self.insert_datos.geometry('400x200')
        self.insert_datos.title("Modificar Datos de Mascota")
        self.insert_datos.resizable(width=0, height=0)

    def config_label(self):  # Labels id, nombre, especie, dueño, descripcion, fecha
        tk.Label(self.insert_datos, text="Nombre: ").place(x=10, y=10, width=100, height=20)
        tk.Label(self.insert_datos, text="Especie: ").place(x=10, y=40, width=100, height=20)
        tk.Label(self.insert_datos, text="Dueño: ").place(x=10, y=70, width=100, height=20)
        tk.Label(self.insert_datos, text="Descripción: ").place(x=10, y=100, width=100, height=20)
        tk.Label(self.insert_datos, text="Fecha: ").place(x=10, y=130, width=100, height=20)

    def config_entry(self):  # Se configuran los inputs   #id, nombre, especie, dueño, descripcion, fecha
        self.entry_nombre = tk.Entry(self.insert_datos)
        self.entry_nombre.place(x=160, y=10, width=200, height=20)
        self.entry_nombre.insert(0, self.row_data[1])
        self.combo_especie = ttk.Combobox(self.insert_datos)
        self.combo_especie.place(x=160, y=40, width=200, height=20)
        self.combo_especie["values"], self.id_esp = self.__fill_combo_especie()
        self.combo_especie.insert(0, self.row_data[2])
        self.combo_dueno = ttk.Combobox(self.insert_datos)
        self.combo_dueno.place(x=160, y=70, width=200, height=20)
        self.combo_dueno["values"], self.id_due = self.__fill_combo_dueno()
        self.combo_dueno.insert(0, self.row_data[3])
        self.entry_descripcion = tk.Entry(self.insert_datos)
        self.entry_descripcion.place(x=160, y=100, width=200, height=20)
        self.entry_descripcion.insert(0, self.row_data[4])
        self.entry_fecha= tk.Entry(self.insert_datos)
        self.entry_fecha.place(x=160, y=130, width=200, height=20)
        self.entry_fecha.insert(0, self.row_data[5])

    def config_button(self):  # Botón aceptar, llama a la función modificar cuando es clickeado.
        tk.Button(self.insert_datos, text="Aceptar",
                  command=self.modificar).place(x=50, y=160, width=200, height=20)

    def modificar(self):  # Insercion en la base de datos.

        sql = """update mascota set nom_masc = %(nombre)s, id_especie = %(especie)s,
                    id_dueno = %(dueno)s, descrip_masc = %(descripcion)s, fecha_nacimiento = %(fecha)s where id_mascota = %(id_mascota)s"""
        self.db.run_sql(sql, {"nombre": self.entry_nombre.get(), "especie": int(self.id_esp[ self.combo_especie.current()]),
                              "dueno": int(self.id_due[self.combo_dueno.current()]), "descripcion": self.entry_descripcion.get(),
                              "fecha": self.entry_fecha.get(), "id_mascota": int(self.row_data[0])})

        self.insert_datos.destroy()
        self.padre.llenar_treeview()

    def __fill_combo_especie(self):
        sql = "select id_especie, nom_esp from especie"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]

    def __fill_combo_dueno(self):
        sql = "select id_dueno, concat(dueno.nom_due, ' ' , dueno.ape_due) as nombre from dueno;"
        self.data = self.db.run_select(sql)
        return [i[1] for i in self.data], [i[0] for i in self.data]
