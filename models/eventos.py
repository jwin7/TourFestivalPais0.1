import json
class Evento:
    def __init__(self, id: int, nombre: str, artista: str, genero:str, ubicacion: int, 
                 hora_inicio: str, hora_fin: str, descripcion: str, imagen: str ):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.ubicacion = ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    def to_json(self):
        return {"id": self.id, 
                "nombre": self.nombre, 
                "artista": self.artista, 
                "genero": self.genero, 
                "ubicacion": self.ubicacion, 
                "hora_inicio": self.hora_inicio, 
                "hora_fin": self.hora_fin, 
                "descripcion": self.descripcion, 
                "imagen": self.imagen}
    
    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        
        id = data["id"]
        nombre = data["nombre"]
        artista = data["artista"]
        genero = data["genero"]
        ubicacion = data["ubicacion"]
        hora_inicio = data["hora_inicio"]
        hora_fin = data["hora_fin"]
        descripcion = data["descripcion"]
        imagen = data["imagen"]
        
        return cls(id, nombre, artista, genero, ubicacion, hora_inicio, hora_fin, descripcion, imagen)
    
class IndiceEventos:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def obtener_evento_por_id(self, id_evento):
        for evento in self.eventos:
            if evento.id == id_evento:
                return evento
        return None

    def obtener_todos_los_eventos(self):
        return self.eventos

    def buscar_eventos_por_nombre(self, nombre):
        resultados = []
        for evento in self.eventos:
            if nombre.lower() in evento.nombre.lower():
                resultados.append(evento)
        return resultados

    def buscar_eventos_por_artista(self, artista):
        resultados = []
        for evento in self.eventos:
            if artista.lower() in evento.artista.lower():
                resultados.append(evento)
        return resultados

    def buscar_eventos_por_genero(self, genero):
        resultados = []
        for evento in self.eventos:
            if genero.lower() in evento.genero.lower():
                resultados.append(evento)
        return resultados

    def filtrar_eventos_por_ubicacion(self, id_ubicacion):
        resultados = []
        for evento in self.eventos:
            if evento.ubicacion == id_ubicacion:
                resultados.append(evento)
        return resultados

    def filtrar_eventos_por_horario(self, hora_inicio, hora_fin):
        resultados = []
        for evento in self.eventos:
            if hora_inicio <= evento.hora_inicio <= hora_fin:
                resultados.append(evento)
        return resultados

    def guardar_en_archivo(self, archivo):
        eventos_json = [evento.to_json() for evento in self.eventos]
        with open(archivo, 'w') as f:
            json.dump(eventos_json, f)
    
    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                eventos_json = json.load(f)
                self.eventos = [Evento.from_json(json_data) for json_data in eventos_json]
        except FileNotFoundError:
            pass
   