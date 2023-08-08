import json
from models.eventos import Evento


class ControladorEventosAsistidos:
    def __init__(self, usuario, modelo_eventos):
        self.usuario = usuario
        self.modelo_eventos = modelo_eventos

    def obtener_eventos_asistidos(self):
        eventos_asistidos = []
        for evento_id in self.usuario.historial_eventos:
            evento = self.modelo_eventos.obtener_evento_por_id(evento_id)
            if evento:
                eventos_asistidos.append(evento)
        return eventos_asistidos

    def obtener_todos_los_eventos(self):
        eventos = []

        try:
            with open("data/eventos.json", "r") as f:
                eventos_json = json.load(f)
                for evento_data in eventos_json["eventos"]:
                    evento = Evento.from_json(json.dumps(evento_data))
                    eventos.append(evento)
        except FileNotFoundError:
            pass

        return eventos