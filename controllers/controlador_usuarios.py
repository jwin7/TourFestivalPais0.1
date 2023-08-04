import models.usuario as modelo_usuario
import models.eventos as modelo_eventos
import views.vista_usuario as vista_usuario

def mostrar_historial_eventos(usuario_id):
    usuario = modelo_usuario.obtener_usuario_por_id(usuario_id)
    eventos_asistidos = modelo_eventos.obtener_eventos_por_ids(usuario.historial_eventos)

    vista_usuario.mostrar_historial(usuario, eventos_asistidos)
