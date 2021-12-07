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
#from jaula import jaula

class App: 
    def __init__(self, db):
        self.db = db
        
        # Main window
        self.root = tk.Tk()
        
        # Algunas especificaciones de tamaño y título de la ventana
        self.root.geometry("700x400")
        self.root.title("Vet patitas")
        
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
        maestros_menu = Menu(menubar, tearoff=False)
        maestros_menu.add_command (label='Medicos',
                                command=self.__mostrar_equipos)
        
        #
        menubar.add_cascade(label="Archivo", menu=file_menu)
        menubar.add_cascade(label="Maestros", menu=maestros_menu)
    
    # botones principales.
    def __crea_botones_principales(self):
        padx = 2
        pady = 2
        
        #
        frame = LabelFrame(self.root, text="", relief=tk.GROOVE)
        frame.place(x=10, y=10, width=200, relheight=0.95) 
        
        # boton medicos menu principal

        b0 = Button(frame, text="Atencion", width=20)
        b0.grid(row=1, column=0, padx=padx, pady=pady)
        b0.bind('<Button-1>', self.__mostrar_medicos)

        b1 = Button(frame, text="Medicos", width=20)
        b1.grid(row=2, column=0, padx=padx, pady=pady)
        b1.bind('<Button-1>', self.__mostrar_medicos)

        #
        b2 = Button(frame, text="Jaulas", width=20)
        b2.grid(row=3, column=0, padx=padx, pady=pady)
        b2.bind('<Button-1>', self.__mostrar_medicos)

        b3 = Button(frame, text="Dueños", width=20)
        b3.grid(row=3, column=0, padx=padx, pady=pady)
        b3.bind('<Button-1>', self.__mostrar_duenos)

        #
        bg = Button(frame, text="Gráfico", width=20)
        bg.grid(row=5, column=0, padx=padx, pady=pady)
        bg.bind('<Button-1>', self.__graficos)
    
    # imagen principal.
    def __agrega_imagen_principal(self):
        #
        frame = LabelFrame(self.root, text="", relief=tk.FLAT)
        frame.place(x=215, y=10, relwidth=0.68, relheight=0.95) 
        
        image = Image.open("futbol.jpg")
        photo = ImageTk.PhotoImage(image.resize((450, 320), Image.ANTIALIAS))
        label = Label(frame, image=photo)
        label.image = photo
        label.pack()

    
    # muestra ventana equipos.
    def __mostrar_equipos(self):
        equipo(self.root, self.db)

    def __mostrar_duenos(self, button):
        dueno(self.root, self.db)
    # muestra ventana jugadores.
    def __mostrar_medicos(self, button):
        medico(self.root, self.db)
    
    def __graficos(self, button):
        graficos(self.root, self.db)

def main():
    # Conecta a la base de datos
    db = Database()
    
    # La app xD
    App(db)

if __name__ == "__main__":
    main()
