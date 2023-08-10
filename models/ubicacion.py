import json

class Ubicacion:
    @staticmethod
    def obtener_todos():
        with open('data/ubicacion.json', 'r') as f:
            data = json.load(f)
            return data