import models.eventos as modelo_eventos
import models.ubicacion as modelo_ubicacion
import views.vista_mapa as vista_mapa
import folium

def mostrar_mapa_eventos():
    eventos = modelo_eventos.cargar_eventos()
    ubicaciones = modelo_ubicacion.cargar_ubicaciones()

    mapa = folium.Map(location=[0, 0], zoom_start=2)  # Crear un mapa vacío

    for evento in eventos:
        ubicacion_evento = next((ubicacion for ubicacion in ubicaciones if ubicacion.id == evento.id_ubicacion), None)
        if ubicacion_evento:
            folium.Marker(
                location=[ubicacion_evento.latitud, ubicacion_evento.longitud],
                popup=f"{evento.nombre} - {evento.artista}",
                icon=folium.Icon(icon='music')
            ).add_to(mapa)

    vista_mapa.mostrar_mapa(mapa)

def planificar_rutas():
    # Aquí puedes implementar la lógica para la planificación de rutas entre eventos
    # Puedes utilizar algoritmos de rutas como el Problema del Viajante (TSP) o Dijkstra
    # y luego mostrar la ruta en el mapa con líneas o rutas optimizadas.

    # Ejemplo básico: Mostrar una ruta simple entre dos eventos (puntos en el mapa)
    evento1 = {"nombre": "Evento1", "latitud": 40.7128, "longitud": -74.0060}
    evento2 = {"nombre": "Evento2", "latitud": 34.0522, "longitud": -118.2437}

    mapa = folium.Map(location=[evento1["latitud"], evento1["longitud"]], zoom_start=5)

    folium.Marker(
        location=[evento1["latitud"], evento1["longitud"]],
        popup=evento1["nombre"],
        icon=folium.Icon(icon='music')
    ).add_to(mapa)

    folium.Marker(
        location=[evento2["latitud"], evento2["longitud"]],
        popup=evento2["nombre"],
        icon=folium.Icon(icon='music')
    ).add_to(mapa)

    folium.PolyLine(
        locations=[[evento1["latitud"], evento1["longitud"]], [evento2["latitud"], evento2["longitud"]]],
        color='blue'
    ).add_to(mapa)

    vista_mapa.mostrar_mapa(mapa)
