import json
from models.ubicacion import Ubicacion
from models.rutaVisita import RutaVisita

class ControladorUbicaciones:
    def cargar_ubicaciones(self):
        ubicaciones = []

        with open('data/ubicacion.json', 'r') as ubicacion_file:
            ubicaciones_data = json.load(ubicacion_file)
            for ubicacion_data in ubicaciones_data['ubicacion']:
                ubicacion = Ubicacion(
                    ubicacion_data['id'],
                    ubicacion_data['direccion'],
                    ubicacion_data['coordenadas'],
                )
                ubicaciones.append(ubicacion)

        return ubicaciones
    

    def crear_ruta(self, nombre, ids_eventos, id_destino):
        nueva_ruta = RutaVisita(len(self.rutas) + 1, nombre, ids_eventos, id_destino)
        self.rutas.append(nueva_ruta)
        self.guardar_rutas_en_archivo()

    def guardar_rutas_en_archivo(self):
        with open('data/rutaVisita.json', 'w') as file:
            data = [ruta.to_json() for ruta in self.rutas]
            json.dump(data, file)
