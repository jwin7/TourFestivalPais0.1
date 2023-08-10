
from tkinter import Frame, Label, Entry, Button, Text
from controllers.controlador_review import ControladorReview

class VistaReview(Frame):
    def __init__(self, master=None, evento=None):
        super().__init__(master)
        self.master = master
        self.evento = evento
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        self.titulo = Label(self, text=f"Escribir reseña para el evento {self.evento['nombre']}")
        self.titulo.pack(side="top")

        self.label_calificacion = Label(self, text="Calificación (1-5):")
        self.label_calificacion.pack(side="top")
        self.entry_calificacion = Entry(self)
        self.entry_calificacion.pack(side="top")

        self.label_comentario = Label(self, text="Comentario:")
        self.label_comentario.pack(side="top")
        self.text_comentario = Text(self)
        self.text_comentario.pack(side="top")

        self.boton_enviar = Button(self, text="Enviar reseña", command=self.enviar_review)
        self.boton_enviar.pack(side="bottom")

    def enviar_review(self):
        calificacion = int(self.entry_calificacion.get())
        comentario = self.text_comentario.get("1.0", "end-1c")
        review = {
            'id_evento': self.evento['id'],
            'calificacion': calificacion,
            'comentario': comentario
        }
        controlador_review = ControladorReview()
        controlador_review.crear_review(review)
