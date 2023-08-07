import json

class ControladorUsuarios:
    def __init__(self):
        with open("data/usuarios.json") as usuarios_file:
            self.usuarios = json.load(usuarios_file)

    def validar_usuario(self, usuario, contrasena):
        for usuario_data in self.usuarios:
            if usuario_data["usuario"] == usuario and usuario_data["contrasena"] == contrasena:
                return True
        return False

    def obtener_eventos_asistidos(self, usuario):
        for usuario_data in self.usuarios:
            if usuario_data["usuario"] == usuario:
                return usuario_data.get("eventos_asistidos", [])
        return []

