#https://matplotlib.org/stable/plot_types/stats/hist_plot.html#sphx-glr-plot-types-stats-hist-plot-py
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from sklearn.datasets import load_iris

class histogram:
    def __init__(self, root, db):

        root = Tk()
        root.title("Histograma Especies de Mascotas Registradas")

        self.root = root
        self.db = db

        fig, ax = plt.subplots()

        x,y = self.__get_data()

        ax.hist(x, bins=10)
        ax.set_xlabel("Tipos Especies")
        canvas = FigureCanvasTkAgg(fig, master = root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        root.mainloop()

    def __get_data(self):

        sql = """SELECT especie.nom_esp, COUNT(mascota.id_especie)
                FROM mascota
                INNER JOIN especie ON mascota.id_especie = especie.id_especie
                GROUP BY mascota.id_especie;"""


        data = self.db.run_select(sql)
        x = [i[0] for i in data]
        y = [i[1] for i in data]
        return x, y
