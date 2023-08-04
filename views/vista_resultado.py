import tkinter as tk

class VistaResultados(tk.Toplevel):
    def __init__(self, eventos):
        super().__init__()
        self.title('Resultados de Búsqueda y Filtrado')

        # Crea una lista o tabla para mostrar los detalles de cada evento
        lista_eventos = tk.Listbox(self, width=50, height=10)

        for evento in eventos:
            nombre = evento.nombre
            artista = evento.artista
            genero = evento.genero
            ubicacion = evento.id_ubicacion

            # Agregar cada evento a la lista o tabla
            lista_eventos.insert(tk.END, f"{nombre} - {artista} - {genero} - Ubicación: {ubicacion}")

        lista_eventos.pack()

        # Ejecutar el bucle principal de la ventana
        self.mainloop()
