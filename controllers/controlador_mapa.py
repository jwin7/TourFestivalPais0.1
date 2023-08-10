
import folium
from models.evento import Evento
from models.ubicacion import Ubicacion

class ControladorMapa:
    def crear_mapa(self):
        # Crear un mapa centrado en Argentina
        mapa = folium.Map(location=[-38.416097, -63.616672], zoom_start=4)

        # Obtener la lista de eventos y ubicaciones
        eventos = Evento.obtener_todos()
        ubicaciones = Ubicacion.obtener_todos()

        # Agregar marcadores al mapa para mostrar la ubicación de los eventos
        for evento in eventos:
            ubicacion = next(ubicacion for ubicacion in ubicaciones if ubicacion['id'] == evento['ubicacion'])
            folium.Marker(
                location=ubicacion['coordenadas'],
                popup=f"{evento['nombre']} - {evento['artista']}"
            ).add_to(mapa)

        return mapa
    
