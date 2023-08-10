
from models.evento import Evento
from models.usuario import Usuario

class ControladorEvento:
    def obtener_eventos(self):
        return Evento.obtener_todos()

    def obtener_eventos_asistidos_por_usuario(self, id_usuario):
        usuario = Usuario.obtener_por_id(id_usuario)
        eventos = Evento.obtener_todos()
        eventos_asistidos = [evento for evento in eventos if evento['id'] in usuario['historial_eventos']]
        return eventos_asistidos

    def obtener_evento_por_id(self, id_evento):
        eventos = Evento.obtener_todos()
        for evento in eventos:
            if evento['id'] == id_evento:
                return evento
