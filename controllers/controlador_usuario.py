
from models.usuario import Usuario

class ControladorUsuario:
    def obtener_usuarios(self):
        return Usuario.obtener_todos()

    def obtener_usuario_por_id(self, id_usuario):
        return Usuario.obtener_por_id(id_usuario)
