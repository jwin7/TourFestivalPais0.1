import tkinter as tk

def mostrar_comentarios(comentarios):
    # Crea la ventana y los elementos de la vista para mostrar los comentarios
    ventana = tk.Toplevel()
    ventana.title("Comentarios y Calificaciones")
    
    # Agrega un widget Label para mostrar los comentarios
    label_titulo = tk.Label(ventana, text="Comentarios y Calificaciones")
    label_titulo.pack()

    for comentario in comentarios:
        # Muestra cada comentario en un widget Label
        label_comentario = tk.Label(ventana, text=comentario)
        label_comentario.pack()

    # Agrega otros elementos y lógica según tus necesidades
    # Por ejemplo, botones para agregar un comentario, calificar un evento, etc.

    # Ejemplo para cerrar la ventana al hacer clic en un botón "Cerrar"
    boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack()

def mostrar_calificar_evento(evento):
    # Crea la ventana y los elementos de la vista para calificar un evento
    ventana = tk.Toplevel()
    ventana.title("Calificar Evento")

    # Agrega elementos para mostrar los detalles del evento y la calificación
    label_titulo = tk.Label(ventana, text="Calificar el evento:")
    label_titulo.pack()

    label_nombre_evento = tk.Label(ventana, text=evento["nombre"])
    label_nombre_evento.pack()

    # Agrega un Entry o combobox para que el usuario seleccione una calificación
    # Y un Entry o Text para que el usuario ingrese un comentario

    # Agrega un botón para enviar la calificación y comentario al controlador correspondiente

    # Ejemplo para cerrar la ventana al hacer clic en un botón "Cerrar"
    boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack()
