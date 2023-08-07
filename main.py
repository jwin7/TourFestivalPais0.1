import json
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import tkinter.scrolledtext as scrolledtext
import tkinter.font as font
from models.eventos import Evento
from models.ubicacion import Ubicacion
from models.review import Review
from models.usuarios import Usuario
from PIL import Image, ImageTk
import requests
from views.vista_inicio import VistaInicio
from views.vista_eventos import VistaEventos
from views.vista_eventos import VistaEvento
from controllers.controlador_usuarios import ControladorUsuarios
from controllers.controlador_eventos import ControladorEventos
from views.vista_inicio import VistaInicio
from views.vista_eventos import VistaEventos
from controllers.controlador_usuarios import ControladorUsuarios

def main():
    vista_inicio = VistaInicio()
    controlador_usuarios = ControladorUsuarios()

    
    usuario = vista_inicio.mostrar_ventana_inicio(controlador_usuarios)

    eventos_asistidos = controlador_usuarios.obtener_eventos_asistidos(usuario)

    if eventos_asistidos:
        vista_eventos = VistaEventos(usuario)
        vista_eventos.mostrar_ventana_eventos(eventos_asistidos)
    else:
        print("No se encontraron eventos asistidos para el usuario")

if __name__ == "__main__":
    main()