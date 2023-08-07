from tkinter import Tk, Label, Listbox
import json
from models.eventos import Evento

class VentanaEventosAsistidos:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario

        self.lista_eventos = Listbox(root)
        self.lista_eventos.pack()

        self.mostrar_eventos_asistidos()

    def mostrar_eventos_asistidos(self):
        eventos_asistidos = self.obtener_eventos_asistidos()

        for evento in eventos_asistidos:
            self.lista_eventos.insert("end", evento.nombre)

    def obtener_eventos_asistidos(self):
        eventos_asistidos = []
        with open("data/eventos.json", "r") as f:
            eventos_json = json.load(f)
            for evento_data in eventos_json["eventos"]:
                if evento_data["id"] in self.usuario.historial_eventos:
                    evento = Evento.from_json(json.dumps(evento_data))
                    eventos_asistidos.append(evento)
        return eventos_asistidos
