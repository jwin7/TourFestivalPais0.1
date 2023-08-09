import tkinter as tk
from controllers.controlador_inicio import ControladorInicio

class VistaInicio:
    def __init__(self, master):
        self.master = master
        self.controlador = ControladorInicio()
        
        self.master.title("TourFestivalPais - Inicio")
        
        self.label_nombre = tk.Label(self.master, text="Nombre:")
        self.label_nombre.grid(row=0, column=0)
        
        self.entry_nombre = tk.Entry(self.master)
        self.entry_nombre.grid(row=0, column=1)
        
        self.label_contrasena = tk.Label(self.master, text="Contraseña:")
        self.label_contrasena.grid(row=1, column=0)
        
        self.entry_contrasena = tk.Entry(self.master, show="*")
        self.entry_contrasena.grid(row=1, column=1)
        
        self.button_iniciar_sesion = tk.Button(self.master, text="Iniciar sesión", command=self.iniciar_sesion)
        self.button_iniciar_sesion.grid(row=2, column=0, columnspan=2)
        
        self.label_mensaje = tk.Label(self.master, text="")
        self.label_mensaje.grid(row=3, column=0, columnspan=2)
    
    def iniciar_sesion(self):
        nombre = self.entry_nombre.get()
        contrasena = self.entry_contrasena.get()
        
        usuario = self.controlador.iniciar_sesion(nombre, contrasena)
        
        if usuario:
            # Inicio de sesión exitoso
            # Mostrar la vista de índice de eventos
            pass
        else:
            # Inicio de sesión fallido
            # Mostrar mensaje de error
            self.label_mensaje.config(text="Nombre o contraseña incorrectos")
