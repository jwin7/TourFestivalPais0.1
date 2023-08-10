
from tkinter import Frame, Label, Listbox, Button
from controllers.controlador_evento import ControladorEvento
from views.vista_resenas import VistaResenas
from views.vista_mapa import VistaMapa

class VistaHistorial(Frame):
    def __init__(self, master=None, usuario=None):
        super().__init__(master)
        self.master = master
        self.usuario = usuario
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.titulo = Label(self, text=f"Historial de eventos asistidos por {self.usuario['nombre']} {self.usuario['apellido']}")
        self.titulo.pack(side="top")

        self.lista_eventos = Listbox(self)
        self.lista_eventos.pack(side="top")

        controlador_evento = ControladorEvento()
        eventos_asistidos = controlador_evento.obtener_eventos_asistidos_por_usuario(self.usuario['id'])
        for evento in eventos_asistidos:
            self.lista_eventos.insert(evento['id'], evento['nombre'])

        self.boton_ver_resenas = Button(self, text="Ver reseñas", command=self.ver_resenas)
        self.boton_ver_resenas.pack(side="bottom")

        self.boton_ver_mapa = Button(self, text="Ver mapa", command=self.ver_mapa)
        self.boton_ver_mapa.pack(side="bottom")


    def ver_resenas(self):
        seleccion = self.lista_eventos.curselection()
        if seleccion:
            id_evento = seleccion[0] + 1
            controlador_evento = ControladorEvento()
            evento = controlador_evento.obtener_evento_por_id(id_evento)

            resenas = VistaResenas(master=self.master, evento=evento)
            resenas.mainloop()

    def ver_mapa(self):
        mapa = VistaMapa(master=self.master)
        mapa.mainloop()