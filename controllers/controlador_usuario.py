import json
from models.usuario import Usuario

class ControladorUsuario:
    def __init__(self):
        with open('data/usuario.json', 'r') as file:
            self.usuarios = json.load(file)

    def obtener_usuarios(self, busqueda=None):
        usuarios = self.usuarios
        if busqueda:
            usuarios = [usuario for usuario in usuarios if busqueda.lower() in usuario.nombre.lower()]
        
        return usuarios

    def obtener_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None
    