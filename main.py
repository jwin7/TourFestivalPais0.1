import customtkinter as tk
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
import json
from views.vista_inicio import VistaInicio
from views.vista_eventos import VistaEventos
from views.vista_eventos import VistaEvento
from controllers.controlador_usuarios import ControladorUsuarios
from controllers.controlador_eventos import ControladorEventos


def main():
    app = App()
    app.mainloop() 

    vista_inicio = VistaInicio()
    controlador_usuarios = ControladorUsuarios()

    # Aquí se inicia la aplicación, por ejemplo, mostrar la ventana de inicio de sesión
    vista_inicio.mostrar_ventana_inicio(controlador_usuarios)

if __name__ == "__main__":
    main()