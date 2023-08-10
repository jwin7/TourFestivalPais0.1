import json

class RutaVisita:
    @staticmethod
    def obtener_todos():
        with open('data/rutaVisita.json', 'r') as f:
            data = json.load(f)
            return data