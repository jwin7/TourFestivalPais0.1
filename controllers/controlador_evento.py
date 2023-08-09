import json
from models.evento import Evento

class ControladorEventos:
    def __init__(self):
        with open('data/evento.json', 'r') as file:
            self.eventos = [Evento.from_json(evento) for evento in json.load(file)]

    def obtener_eventos(self, busqueda=None, filtros=None):
        eventos = self.eventos
        if busqueda:
            eventos = [evento for evento in eventos if busqueda.lower() in evento.nombre.lower()]
        if filtros:
            if 'genero' in filtros:
                eventos = [evento for evento in eventos if evento.genero == filtros['genero']]
            if 'artista' in filtros:
                eventos = [evento for evento in eventos if evento.artista == filtros['artista']]
            if 'ubicacion' in filtros:
                eventos = [evento for evento in eventos if evento.id_ubicacion == filtros['ubicacion']]
            if 'horario' in filtros:
                eventos = [evento for evento in eventos if evento.hora_inicio >= filtros['horario'][0] and evento.hora_fin <= filtros['horario'][1]]
        return eventos

    def obtener_evento(self, id_evento):
        for evento in self.eventos:
            if evento.id == id_evento:
                return evento
        return None