import tkinter as tk

def mostrar_resultados(eventos):
    # Crea una ventana para mostrar los resultados de búsqueda y filtrado
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title('Resultados de Búsqueda y Filtrado')

    # Crea una lista o tabla para mostrar los detalles de cada evento
    lista_eventos = tk.Listbox(ventana_resultados, width=50, height=10)

    for evento in eventos:
        nombre = evento.nombre
        artista = evento.artista
        genero = evento.genero
        ubicacion = evento.id_ubicacion

        # Agregar cada evento a la lista o tabla
        lista_eventos.insert(tk.END, f"{nombre} - {artista} - {genero} - Ubicación: {ubicacion}")

    lista_eventos.pack()

    # Ejecutar el bucle principal de la ventana
    ventana_resultados.mainloop()
