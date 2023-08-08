import json
class Review:
    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_json(self):
        return {
            "id": self.id,
            "id_evento": self.id_evento,
            "id_usuario": self.id_usuario,
            "calificacion": self.calificacion,
            "comentario": self.comentario,
            "animo": self.animo
        }    
    
    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(
            data["id"],
            data["id_evento"],
            data["id_usuario"],
            data["calificacion"],
            data["comentario"],
            data["animo"]
            )
    
class IndiceReviews:
    def __init__(self):
        self.reviews = []

    def agregar_review(self, review):
        self.reviews.append(review)

    def obtener_reviews_por_usuario(self, id_usuario):
        reviews_usuario = []
        for review in self.reviews:
            if review.id_usuario == id_usuario:
                reviews_usuario.append(review)
        return reviews_usuario

    def obtener_reviews_por_evento(self, id_evento):
        reviews_evento = []
        for review in self.reviews:
            if review.id_evento == id_evento:
                reviews_evento.append(review)
        return reviews_evento

    def guardar_en_archivo(self, archivo):
        reviews_json = [review.to_json() for review in self.reviews]
        with open(archivo, 'w') as f:
            json.dump(reviews_json, f)
    
    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                reviews_json = json.load(f)
                self.reviews = [Review.from_json(json_data) for json_data in reviews_json]
        except FileNotFoundError:
            pass
