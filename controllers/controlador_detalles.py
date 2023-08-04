import models.eventos as modelo_eventos
import models.review as modelo_review
import views.vista_detalles as vista_detalles

def mostrar_detalles_evento(evento_id):
    evento = modelo_eventos.obtener_evento_por_id(evento_id)
    reseñas = modelo_review.obtener_reseñas_por_evento(evento_id)

    vista_detalles.mostrar_detalles(evento, reseñas)

def escribir_reseña(evento_id, usuario_id, calificacion, comentario, animo):
    # Aquí puedes agregar validaciones y lógica para evitar duplicados, etc.
    modelo_review.agregar_reseña(evento_id, usuario_id, calificacion, comentario, animo)
    mostrar_detalles_evento(evento_id)

    modelo_review.agregar_reseña(evento_id, usuario_id, int(calificacion), comentario, animo)
    mostrar_detalles_evento(evento_id)