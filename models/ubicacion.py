import json

class Ubicacion:
    def __init__(self, id: int, nombre: str, direccion: str, latitud: float, longitud: float):
        self.id = id
        self.nombre = nombre  
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud
        
    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "direccion": self.direccion, "latitud": self.latitud, "longitud": self.longitud}
    

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        nombre = data["nombre"]
        direccion = data["direccion"]
        latitud = data["latitud"]
        longitud = data["longitud"]
        
        return cls(id, nombre, direccion, latitud, longitud)
    
        