
from tkinter import Frame, Label, Button, Listbox
from controllers.controlador_usuario import ControladorUsuario
from views.vista_historial import VistaHistorial

class VistaInicio(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.titulo = Label(self, text="Bienvenido a la aplicación de eventos")
        self.titulo.pack(side="top")

        self.lista_usuarios = Listbox(self)
        self.lista_usuarios.pack(side="top")

        controlador_usuario = ControladorUsuario()
        usuarios = controlador_usuario.obtener_usuarios()
        for usuario in usuarios:
            self.lista_usuarios.insert(usuario['id'], f"{usuario['nombre']} {usuario['apellido']}")

        self.boton_ver_historial = Button(self, text="Ver historial de eventos asistidos", command=self.ver_historial)
        self.boton_ver_historial.pack(side="bottom")

    def ver_historial(self):
        id_usuario = self.lista_usuarios.curselection()[0] + 1
        controlador_usuario = ControladorUsuario()
        usuario = controlador_usuario.obtener_usuario_por_id(id_usuario)

        historial = VistaHistorial(master=self.master, usuario=usuario)
        historial.mainloop()
