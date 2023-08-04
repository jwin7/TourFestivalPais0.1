import json
class Evento:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen



def cargar_eventos():
    with open('data/eventos.json', 'r') as file:
        data = json.load(file)
        eventos = []
        for evento_data in data['eventos']:
            evento = Evento(
                id=evento_data['id'],
                nombre=evento_data['nombre'],
                artista=evento_data['artista'],
                genero=evento_data['genero'],
                id_ubicacion=evento_data['id_ubicacion'],
                hora_inicio=evento_data['hora_inicio'],
                hora_fin=evento_data['hora_fin'],
                descripcion=evento_data['descripcion'],
                imagen=evento_data['imagen']
            )
            eventos.append(evento)
        return eventos
