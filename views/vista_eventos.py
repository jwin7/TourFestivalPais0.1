import json

import tkinter as tk

class VistaEventos:
    def __init__(self, usuario):
        self.root = tk.Tk()
        self.root.title("Eventos de {}".format(usuario))
        self.eventos_listbox = tk.Listbox(self.root)

    def mostrar_ventana_eventos(self, eventos_asistidos):
        for evento in eventos_asistidos:
            self.eventos_listbox.insert(tk.END, evento)

        self.eventos_listbox.pack()

        self.root.mainloop()
