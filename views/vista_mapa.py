import io
import folium
import branca
from tkinter import Frame, Label, Canvas
from controllers.controlador_mapa import ControladorMapa
import tkinter as tk
from tkinter import scrolledtext

class VistaMapa(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        controlador_mapa = ControladorMapa()
        mapa = controlador_mapa.crear_mapa()

        # Crear un objeto Figure para contener el mapa
        figura = branca.element.Figure()
        figura.add_child(mapa)

        # Generar el código HTML del mapa
        html = figura.render()

        # Crear un widget HTMLLabel para mostrar el mapa
        label = HTMLLabel(self)
        label.pack(fill="both", expand=True)
        label.set_html(html)

class HTMLLabel(scrolledtext.ScrolledText):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(state=tk.DISABLED)

    def set_html(self, html):
        self.config(state=tk.NORMAL)
        self.delete('1.0', tk.END)
        self.insert(tk.INSERT, html)
        self.config(state=tk.DISABLED)
