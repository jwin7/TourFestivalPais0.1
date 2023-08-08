import json

class Usuario:
    def __init__(self, id, nombre, apellido, contrasena, historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.contrasena = contrasena
        self.historial_eventos = historial_eventos

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "contrasena": self.contrasena,
            "historial_eventos": self.historial_eventos
        }
    
    @classmethod
    def from_json(cls, data):
        return cls(
            data["id"],
            data["nombre"],
            data["apellido"],
            data["contrasena"],
            data["historial_eventos"]
        )

    