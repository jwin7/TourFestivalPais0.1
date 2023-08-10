
import json

class Evento:
    @staticmethod
    def obtener_todos():
        with open('data/evento.json', 'r') as f:
            data = json.load(f)
            return data
