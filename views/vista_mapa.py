import tkinter as tk
from tkinter import ttk
import folium
from models.ubicacion import Ubicacion

class VistaMapa:
    def __init__(self, root, ubicaciones):
        self.root = root
        self.ubicaciones = ubicaciones

        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.map_frame = ttk.Frame(self.frame)
        self.map_frame.pack(fill=tk.BOTH, expand=True)
        self.create_map()

    def create_map(self):
        m = folium.Map(location=[-34.6099, -58.3965], zoom_start=12)  # Coordenadas de Buenos Aires, Argentina

        for ubicacion in self.ubicaciones:
            folium.Marker(
                location=[ubicacion.latitud, ubicacion.longitud],
                popup=ubicacion.nombre
            ).add_to(m)

        
        map_canvas = folium.Map(location=[0, 0], zoom_start=1).get_root().canvas()
        map_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Si deseas ejecutar esta vista de manera independiente para probarla:
if __name__ == "__main__":

    ubicaciones = [
        Ubicacion(1, "Ubicación 1", "Dirección 1", -34.6099, -58.3965),
        Ubicacion(2, "Ubicación 2", "Dirección 2", -34.6000, -58.3900),
        # ... Agregar más ubicaciones
    ]

    root = tk.Tk()
    root.title("Vista de Mapa")

    vista_mapa = VistaMapa(root, ubicaciones)

    root.mainloop()
