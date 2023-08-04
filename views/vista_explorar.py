import tkinter as tk
import views.vista_eventos as vista_eventos

class VistaExplorar(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Explorar Eventos")

        # Agregar elementos y lógica para la vista de explorar
        # Por ejemplo, puedes mostrar una lista de eventos y permitir al usuario filtrarlos o buscarlos
        vista_eventos.mostrar_lista_eventos()
        # Ejemplo para agregar un botón "Cerrar" y asociar el comando para cerrar la ventana
        boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        boton_cerrar.pack()

    def ocultar(self):
        # Esta función oculta la ventana de la vista de explorar
        # Puedes usarla cuando el usuario navega a otra sección de la aplicación
        self.withdraw()


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
