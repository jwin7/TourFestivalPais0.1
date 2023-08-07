from tkinter import Tk, Label, Entry, Button, messagebox
import json
from models.usuario import Usuario
from views.vista_eventos import VentanaEventosAsistidos
class VentanaInicio:
    def __init__(self, root):
        self.root = root
        self.usuarios = self.cargar_usuarios()

        self.label_usuario = Label(root, text="Usuario:")
        self.entry_usuario = Entry(root)
        self.label_contrasena = Label(root, text="Contraseña:")
        self.entry_contrasena = Entry(root, show="*")
        self.boton_iniciar_sesion = Button(root, text="Iniciar Sesión", command=self.iniciar_sesion)

        self.label_usuario.pack()
        self.entry_usuario.pack()
        self.label_contrasena.pack()
        self.entry_contrasena.pack()
        self.boton_iniciar_sesion.pack()

    def cargar_usuarios(self):
        with open("data/usuario.json", "r") as f:
            usuarios_json = json.load(f)
            usuarios = [Usuario.from_json(json.dumps(usuario_data)) for usuario_data in usuarios_json["usuarios"]]
        return usuarios

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        # Validar las credenciales con los datos almacenados
        for u in self.usuarios:
            if u.nombre == usuario and u.contrasena == contrasena:
                self.abrir_ventana_eventos_asistidos(u)
                return

        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def abrir_ventana_eventos_asistidos(self, usuario):
        self.root.destroy()  # Cerrar la ventana de inicio de sesión
        root_eventos_asistidos = Tk()
        root_eventos_asistidos.title("Eventos Asistidos")
        root_eventos_asistidos.geometry("400x300")

        ventana_eventos_asistidos = VentanaEventosAsistidos(root_eventos_asistidos, usuario)
        #root_eventos_asistidos.mainloop()
