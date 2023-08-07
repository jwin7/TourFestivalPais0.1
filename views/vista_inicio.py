import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import tkinter.scrolledtext as scrolledtext
import tkinter.font as font
from PIL import Image, ImageTk
import requests
import json
import controllers.controlador_usuarios as ControladorUsuarios

class VistaInicio:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inicio de Sesión")
        self.usuario_entry = tk.Entry(self.root)
        self.contrasena_entry = tk.Entry(self.root, show="*")
        self.iniciar_sesion_button = tk.Button(self.root, text="Iniciar sesión", command=self.iniciar_sesion)

    def mostrar_ventana_inicio(self, ControladorUsuarios):
        #// Aquí se colocaría el diseño de la ventana?
        self.ControladorUsuarios()
        self.root.mainloop()

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        if ControladorUsuarios.validar_usuario(usuario, contrasena):
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
            self.mostrar_ventana_eventos()  # Método para mostrar la ventana de eventos (por implementar)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def mostrar_ventana_eventos(self):
        # Método para mostrar la ventana de eventos (por implementar)
        pass
