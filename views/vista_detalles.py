import tkinter as tk
from tkinter import ttk
from controllers import controlador_detalles  # Asegúrate de que el nombre sea correcto y esté en el lugar adecuado


def mostrar_detalles(evento, reseñas):
    # Crea una ventana para mostrar los detalles del evento y las reseñas
    ventana_detalles = tk.Toplevel()
    ventana_detalles.title(f"Detalles de {evento.nombre}")

    # Mostrar detalles del evento
    etiqueta_nombre = tk.Label(ventana_detalles, text=f"Nombre: {evento.nombre}")
    etiqueta_artista = tk.Label(ventana_detalles, text=f"Artista: {evento.artista}")
    etiqueta_genero = tk.Label(ventana_detalles, text=f"Género: {evento.genero}")
    etiqueta_descripcion = tk.Label(ventana_detalles, text=f"Descripción: {evento.descripcion}")
    etiqueta_horario = tk.Label(ventana_detalles, text=f"Horario: {evento.hora_inicio} - {evento.hora_fin}")
    # Agregar más detalles si lo deseas

    etiqueta_nombre.pack()
    etiqueta_artista.pack()
    etiqueta_genero.pack()
    etiqueta_descripcion.pack()
    etiqueta_horario.pack()
    # Pack más detalles si los agregas

    # Mostrar reseñas y calificaciones
    etiqueta_resenas = tk.Label(ventana_detalles, text="Reseñas y Calificaciones")
    etiqueta_resenas.pack()

    for reseña in reseñas:
        etiqueta_resena = tk.Label(ventana_detalles, text=f"Calificación: {reseña.calificacion} - Comentario: {reseña.comentario} - Ánimo: {reseña.animo}")
        etiqueta_resena.pack()

    # Agregar un formulario para escribir una nueva reseña y calificación
    etiqueta_nueva_resena = tk.Label(ventana_detalles, text="Escribir una nueva reseña:")
    etiqueta_nueva_resena.pack()

    entrada_calificacion = tk.Entry(ventana_detalles, width=5)
    entrada_calificacion.pack()

    entrada_comentario = tk.Entry(ventana_detalles, width=50)
    entrada_comentario.pack()

    boton_enviar_resena = tk.Button(ventana_detalles, text="Enviar Reseña", command=lambda: enviar_resena(evento.id, entrada_calificacion.get(), entrada_comentario.get(), "Positivo"))
    boton_enviar_resena.pack()

    # Ejecutar el bucle principal de la ventana
    ventana_detalles.mainloop()

    etiqueta_nueva_resena = tk.Label(ventana_detalles, text="Escribir una nueva reseña:")
    etiqueta_nueva_resena.pack()

    entrada_calificacion = tk.Entry(ventana_detalles, width=5)
    entrada_calificacion.pack()

    entrada_comentario = tk.Entry(ventana_detalles, width=50)
    entrada_comentario.pack()

    # Añadir el botón de selección de ánimo
    opcion_animo = tk.StringVar()
    etiqueta_animo = tk.Label(ventana_detalles, text="Seleccionar ánimo del comentario:")
    etiqueta_animo.pack()

    radio_positivo = tk.Radiobutton(ventana_detalles, text="Positivo", variable=opcion_animo, value="Positivo")
    radio_positivo.pack()

    radio_negativo = tk.Radiobutton(ventana_detalles, text="Negativo", variable=opcion_animo, value="Negativo")
    radio_negativo.pack()

    boton_enviar_resena = tk.Button(ventana_detalles, text="Enviar Reseña", command=lambda: enviar_resena(evento.id, entrada_calificacion.get(), entrada_comentario.get(), opcion_animo.get()))
    boton_enviar_resena.pack()

def enviar_resena(evento_id, calificacion, comentario, animo):
    # Puedes agregar validaciones para asegurarte de que los datos sean correctos antes de enviar la reseña
    # Aquí también necesitarás el ID del usuario que está enviando la reseña, lo puedes obtener del sistema de autenticación

    controlador_detalles.escribir_reseña(evento_id, usuario_id, int(calificacion), comentario, animo)
