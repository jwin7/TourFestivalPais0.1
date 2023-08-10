
from models.review import Review

class ControladorReview:
    def crear_review(self, review):
        Review.crear(review)

    def obtener_resenas_por_evento(self, id_evento):
        resenas = Review.obtener_todos()
        resenas_evento = [resena for resena in resenas if resena['id_evento'] == id_evento]
        return resenas_evento