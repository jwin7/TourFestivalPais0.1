import json

class Ubicacion:
    def __init__(self, id: int, direccion: str, coordenadas: float):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas
        
    def to_json(self):
        return {"id": self.id, "direccion": self.direccion, "coordenadas": self.coordenadas}
    

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        direccion = data["direccion"]
        coordenadas = data["coordenadas"]
        
        return cls(id, direccion, coordenadas)
    