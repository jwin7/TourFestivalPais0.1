
from tkinter import Frame, Label, Listbox
from controllers.controlador_review import ControladorReview

class VistaResenas(Frame):
    def __init__(self, master=None, evento=None):
        super().__init__(master)
        self.master = master
        self.evento = evento
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.titulo = Label(self, text=f"Reseñas del evento {self.evento['nombre']}")
        self.titulo.pack(side="top")

        self.lista_resenas = Listbox(self)
        self.lista_resenas.pack(side="top")

        controlador_review = ControladorReview()
        resenas = controlador_review.obtener_resenas_por_evento(self.evento['id'])
        for resena in resenas:
            self.lista_resenas.insert(resena['id'], f"{resena['calificacion']} - {resena['comentario']}")
