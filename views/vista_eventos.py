import tkinter as tk

def mostrar_lista_eventos(eventos):
    # Crea la ventana y los elementos de la vista para mostrar la lista de eventos
    ventana = tk.Toplevel()
    ventana.title("Lista de Eventos")

    # Crea un widget Listbox para mostrar la lista de eventos
    listbox_eventos = tk.Listbox(ventana, width=50)
    listbox_eventos.pack()

    for evento in eventos:
        # Agrega cada evento a la lista
        listbox_eventos.insert(tk.END, f"{evento['nombre']} - {evento['artista']}")

    # Agrega un botón para ver los detalles de un evento seleccionado
    boton_ver_detalles = tk.Button(ventana, text="Ver Detalles", command=lambda: ver_detalles_evento(eventos[listbox_eventos.curselection()[0]]))
    boton_ver_detalles.pack()

    # Ejemplo para cerrar la ventana al hacer clic en un botón "Cerrar"
    boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack()

def ver_detalles_evento(evento):
    # Esta función se ejecuta cuando se hace clic en el botón "Ver Detalles"
    # Crea una ventana nueva para mostrar los detalles del evento
    # Puedes usar el controlador correspondiente para mostrar los detalles del evento en esta nueva ventana
    controlador_eventos.mostrar_detalles_evento(evento["id"])
