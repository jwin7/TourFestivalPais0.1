import tkinter as tk
from tkinter import ttk
import folium
from folium import plugins

def mostrar_mapa(eventos, ubicaciones):
    # Crear la ventana y los elementos de la vista para mostrar el mapa
    ventana = tk.Toplevel()
    ventana.title("Mapa de Eventos")

    # Crear un widget de mapa con folium
    mapa = folium.Map(location=[-34.603722, -58.381592], zoom_start=5)

    for evento in eventos:
        # Agregar un marcador en el mapa para cada ubicación de evento
        ubicacion = ubicaciones[evento["id_ubicacion"]]
        folium.Marker(location=[ubicacion["latitud"], ubicacion["longitud"]],
                      popup=evento["nombre"]).add_to(mapa)

    # Agregar funcionalidad de agrupación de marcadores
    plugins.MarkerCluster().add_to(mapa)

    # Guardar el mapa como un archivo HTML temporal
    mapa.save("temp_mapa.html")

    # Crear el widget WebView en Tkinter para mostrar el mapa
    webview = ttk.Frame(ventana)
    webview.grid(row=0, column=0, padx=10, pady=10)
    webview_mapa = tk.WebView(master=webview)
    webview_mapa.pack(fill=tk.BOTH, expand=tk.YES)
    webview_mapa.set_url("temp_mapa.html")

    # Ejemplo para cerrar la ventana al hacer clic en un botón "Cerrar"
    boton_cerrar = ttk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.grid(row=1, column=0, padx=10, pady=10)

    # Ejemplo para eliminar el archivo HTML temporal al cerrar la ventana
    ventana.protocol("WM_DELETE_WINDOW", lambda: eliminar_archivo_temporal("temp_mapa.html"))

def eliminar_archivo_temporal(nombre_archivo):
    import os
    try:
        os.remove(nombre_archivo)
    except FileNotFoundError:
        pass
