import json

class Review:
    @staticmethod
    def obtener_todos():
        with open('data/review.json', 'r') as f:
            data = json.load(f)
            return data

    @staticmethod
    def crear(review):
        # Cargar los datos actuales
        with open('data/review.json', 'r') as f:
            data = json.load(f)

        # Agregar la nueva reseña
        data.append(review)

        # Guardar los datos actualizados
        with open('data/review.json', 'w') as f:
            json.dump(data, f)