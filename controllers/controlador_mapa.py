import json
from models.ubicacion import Ubicacion

class ControladorUbicaciones:
    def cargar_ubicaciones(self):
        ubicaciones = []

        with open('data/ubicacion.json', 'r') as ubicacion_file:
            ubicaciones_data = json.load(ubicacion_file)
            for ubicacion_data in ubicaciones_data['ubicacion']:
                ubicacion = Ubicacion(
                    ubicacion_data['id'],
                    ubicacion_data['nombre'],
                    ubicacion_data['direccion'],
                    ubicacion_data['latitud'],
                    ubicacion_data['longitud']
                )
                ubicaciones.append(ubicacion)

        return ubicaciones
