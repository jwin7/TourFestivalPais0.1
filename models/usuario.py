import json

class Usuario:
    @staticmethod
    def obtener_todos():
        with open('data/usuario.json', 'r') as f:
            data = json.load(f)
            return data

    @staticmethod
    def obtener_por_id(id_usuario):
        with open('data/usuario.json', 'r') as f:
            data = json.load(f)
            for usuario in data:
                if usuario['id'] == id_usuario:
                    return usuario