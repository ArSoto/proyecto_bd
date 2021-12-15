import tkinter as tk
from tkinter import Menu
from tkinter import LabelFrame, Label, Frame
from tkinter import Button
from PIL import Image, ImageTk

#
from database import Database
from graficos import graficos
from medico import medico
from dueno import dueno
from pabellon import pabellon
from mascota import mascota
from jaula import jaula
from serviciocopia import servicio
#from servicio import servicio
from especie import especie
from histogram import histogram


class App:
    def __init__(self, db):
        self.db = db

        # Main window
        self.root = tk.Tk()

        # Algunas especificaciones de tamaño y título de la ventana
        self.root.geometry("700x400")
        self.root.title("Veterinaria Patitas")

        #
        self.__crea_menubar()
        self.__crea_botones_principales()
        self.__agrega_imagen_principal()

        # Empieza a correr la interfaz.
        self.root.mainloop()

    # menubar
    def __crea_menubar(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        #
        file_menu = Menu(menubar, tearoff=False)
        file_menu.add_command (label='Salir',
                                command=self.root.destroy)
        #
        menubar.add_cascade(label="Opciones", menu=file_menu)

    # botones principales.
    def __crea_botones_principales(self):
        padx = 2
        pady = 2

        #
        frame = LabelFrame(self.root, text="Menú Principal", relief=tk.GROOVE)
        frame.place(x=10, y=10, width=200, relheight=0.95)

        # boton medicos menu principal

        #b0 = Button(frame, text="Prueba", width=20)
        #b0.grid(row=1, column=0, padx=padx, pady=pady)
        #b0.bind('<Button-1>', self.__mostrar_medicos)

        b1 = Button(frame, text="Médicos", width=20)
        b1.grid(row=2, column=0, padx=padx, pady=pady)
        b1.bind('<Button-1>', self.__mostrar_medicos)

        #
        b2 = Button(frame, text="Jaulas", width=20)
        b2.grid(row=3, column=0, padx=padx, pady=pady)
        b2.bind('<Button-1>', self.__mostrar_jaulas)

        b3 = Button(frame, text="Dueños", width=20)
        b3.grid(row=4, column=0, padx=padx, pady=pady)
        b3.bind('<Button-1>', self.__mostrar_duenos)

        b4 = Button(frame, text="Mascotas", width=20)
        b4.grid(row=5, column=0, padx=padx, pady=pady)
        b4.bind('<Button-1>', self.__mostrar_mascotas)

        b9 = Button(frame, text="Especies", width=20)
        b9.grid(row=6, column=0, padx=padx, pady=pady)
        b9.bind('<Button-1>', self.__mostrar_especies)

        b5 = Button(frame, text="Servicio", width=20)
        b5.grid(row=10, column=0, padx=padx, pady=pady)
        b5.bind('<Button-1>', self.__mostrar_servicio)

        #
        bg = Button(frame, text="Pabellón", width=20)
        bg.grid(row=7, column=0, padx=padx, pady=pady)
        bg.bind('<Button-1>', self.__mostrar_pabellon)

        b10 = Button(frame, text="Histograma", width=20)
        b10.grid(row=11, column=0, padx=padx, pady=pady)
        b10.bind('<Button-1>', self.__mostrar_histograma)

    # imagen principal.
    def __agrega_imagen_principal(self):
        #
        frame = LabelFrame(self.root, text="Cuidamos tu mascota, cuidamos tu familia", relief=tk.FLAT)
        frame.place(x=215, y=10, relwidth=0.68, relheight=0.95)

        image = Image.open("vet_logo.jpg")
        photo = ImageTk.PhotoImage(image.resize((450, 320), Image.ANTIALIAS))
        label = Label(frame, image=photo)
        label.image = photo
        label.pack()


    # muestra ventanas
    def __mostrar_duenos(self, button):
        dueno(self.root, self.db)

    def __mostrar_medicos(self, button):
        medico(self.root, self.db)

    def __mostrar_mascotas(self, button):
        mascota(self.root, self.db)

    def __mostrar_jaulas(self, button):
        jaula(self.root, self.db)

    def __mostrar_especies(self, button):
        especie(self.root, self.db)

    def __mostrar_pabellon(self, button):
        pabellon(self.root, self.db)

    def __mostrar_servicio(self, button):
        servicio(self.root, self.db)

    def __mostrar_histograma(self, button):
        histogram(self.root, self.db)



def main():
    # Conecta a la base de datos
    db = Database()

    # Llamado a la app
    App(db)

if __name__ == "__main__":
    main()