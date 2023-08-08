from tkinter import Tk, Listbox
import json
from models.eventos import Evento
from controllers.controlador_eventos import ControladorEventosAsistidos
import tkinter as tk
from tkinter import ttk

class VentanaEventosAsistidos:
    def __init__(self, root, usuario, modelo_eventos): 
        self.root = root
        self.usuario = usuario
        self.modelo_eventos = modelo_eventos  

        self.lista_eventos = Listbox(root)
        self.lista_eventos.pack()

        self.controlador_eventos = ControladorEventosAsistidos(usuario)  
        self.mostrar_eventos_asistidos()

        boton_mostrar_todos = ttk.Button(
            root,
            text="Mostrar Todos los Eventos",
            command=self.mostrar_todos_los_eventos
        )
        boton_mostrar_todos.pack()

    def mostrar_eventos_asistidos(self):
        eventos_asistidos = self.obtener_eventos_asistidos()

        for evento in eventos_asistidos:
            self.lista_eventos.insert("end", evento.nombre)

    def obtener_eventos_asistidos(self):
        return self.controlador_eventos.obtener_eventos_asistidos()

    def mostrar_todos_los_eventos(self):
        eventos = self.controlador_eventos.obtener_todos_los_eventos()

        print("Todos los eventos:")
        for evento in eventos:
            print(f"Evento: {evento.nombre}")

