import tkinter as tk
import views.vista_eventos as vista_eventos

def mostrar_eventos():
    # Aquí puedes obtener los datos de los eventos desde el archivo JSON o desde la base de datos
    # Por simplicidad, aquí creamos una lista de eventos de ejemplo
    eventos = [
        {"id": 1, "nombre": "Evento 1", "artista": "Artista 1", "genero": "Rock"},
        {"id": 2, "nombre": "Evento 2", "artista": "Artista 2", "genero": "Pop"},
        # Agrega más eventos aquí
    ]
    vista_eventos.mostrar_lista_eventos(eventos)

def mostrar_detalles_evento(evento_id):
    # Aquí puedes obtener los detalles del evento con el ID especificado desde el archivo JSON o desde la base de datos
    # Por simplicidad, aquí creamos un evento de ejemplo
    evento = {
        "id": evento_id,
        "nombre": "Evento de ejemplo",
        "artista": "Artista de ejemplo",
        "genero": "Rock",
        "descripcion": "Descripción del evento de ejemplo",
        # Agrega más detalles del evento aquí
    }
    vista_eventos.mostrar_detalles_evento(evento)
