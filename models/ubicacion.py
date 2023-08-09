import json

class Ubicacion:
    def __init__(self, id: int, direccion: str, latitud: float, longitud: float):
        self.id = id
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud
        
    def to_json(self):
        return {"id": self.id, "direccion": self.direccion, "latitud": self.latitud, "longitud": self.longitud}
    

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        direccion = data["direccion"]
        latitud = data["latitud"]
        longitud = data["longitud"]
        
        return cls(id, direccion, latitud, longitud)