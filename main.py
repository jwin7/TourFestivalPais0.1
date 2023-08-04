import tkinter as tk
import controllers.controlador_inicio as controlador_inicio
import controllers.controlador_explorar as controlador_explorar
import controllers.controlador_detalles as controlador_detalles
import controllers.controlador_usuarios as controlador_usuarios

class TourMusicalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tour Festival Pais")
        self.geometry("800x600")

        # Aquí se puede definir la paleta de colores y otros estilos de la interfaz gráfica

        # Agregar una barra de menú si es necesario

        # Agregar botones o widgets para navegar entre las diferentes secciones de la aplicación
        boton_inicio = tk.Button(self, text="Inicio", command=self.mostrar_inicio)
        boton_inicio.pack()

        boton_explorar = tk.Button(self, text="Explorar Eventos", command=self.mostrar_explorar)
        boton_explorar.pack()

        # agregar más botones para otras secciones

        # Mostrar la vista de inicio al iniciar la aplicación
        self.mostrar_inicio()

    def mostrar_inicio(self):
        # Mostrar la vista de inicio
        controlador_inicio.mostrar_inicio()

    def mostrar_explorar(self):
        # Mostrar la vista de explorar eventos
        controlador_explorar.mostrar_explorar()

    # definir más métodos para mostrar otras vistas de la aplicación

if __name__ == "__main__":
    app = TourMusicalApp()
    app.mainloop()
