import json
from models.usuario import Usuario

class ControladorInicio:
    def __init__(self):
        with open('data/usuario.json', 'r') as file:
            self.usuarios = json.load(file)

    def iniciar_sesion(self, nombre, contrasena):
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.contrasena == contrasena:
                return usuario
        return None
    