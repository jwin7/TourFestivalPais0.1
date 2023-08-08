import json

class RutaVisita:
    def __init__(self, id:int, nombre: str, destino: list[int]) :
        self.id = id
        self.nombre = nombre
        self.destino = destino

    def to_json(self):
        return {"id": self.id, "nombre": self.nombre, "destino": self.destino}

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        nombre = data["nombre"]
        destino = data["destino"]
        
        return cls(id, nombre, destino)    
    
class PlanificadorRutas:
    def __init__(self):
        self.rutas = []

    def agregar_ruta(self, ruta):
        self.rutas.append(ruta)

    def obtener_ruta_por_id(self, id_ruta):
        for ruta in self.rutas:
            if ruta.id == id_ruta:
                return ruta
        return None

    def planificar_ruta(self, lista_eventos):
        ruta = []
        
        # Obtén la información de ubicación de los eventos
        ubicaciones = {}  # Un diccionario para almacenar las ubicaciones de los eventos por ID
        with open('data/eventos.json', 'r') as eventos_file:
            eventos_data = json.load(eventos_file)
            for evento in eventos_data['eventos']:
                if evento['id'] in lista_eventos:
                    ubicaciones[evento['id']] = evento['id_ubicacion']
        
        # Crea la ruta basada en las ubicaciones de los eventos
        for evento_id in lista_eventos:
            if evento_id in ubicaciones:
                ruta.append(ubicaciones[evento_id])
        
        # Devuelve la ruta planificada
        return ruta

    def guardar_en_archivo(self, archivo):
        rutas_json = [ruta.to_json() for ruta in self.rutas]
        with open(archivo, 'w') as f:
            json.dump(rutas_json, f)
    
    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                rutas_json = json.load(f)
                self.rutas = [RutaVisita.from_json(json_data) for json_data in rutas_json]
        except FileNotFoundError:
            pass    