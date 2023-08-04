import tkinter as tk

def mostrar_historial(usuario, eventos_asistidos):
    # Crea una ventana para mostrar el historial de eventos asistidos por el usuario
    ventana_historial = tk.Toplevel()
    ventana_historial.title(f"Historial de Eventos Asistidos de {usuario.nombre}")

    # Mostrar la lista de eventos asistidos
    etiqueta_titulo = tk.Label(ventana_historial, text="Historial de Eventos Asistidos")
    etiqueta_titulo.pack()

    if not eventos_asistidos:
        etiqueta_vacio = tk.Label(ventana_historial, text="Aún no has asistido a ningún evento.")
        etiqueta_vacio.pack()
    else:
        for evento in eventos_asistidos:
            etiqueta_evento = tk.Label(ventana_historial, text=f"Nombre: {evento.nombre} - Artista: {evento.artista} - Género: {evento.genero}")
            etiqueta_evento.pack()

    # Ejecutar el bucle principal de la ventana
    ventana_historial.mainloop()
