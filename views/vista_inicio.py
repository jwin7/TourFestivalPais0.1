import tkinter as tk

class VistaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Página de Inicio")

        # Agrega elementos de la página de inicio, como botones para navegar a otras secciones, etc.

        # Ejemplo para cerrar la ventana al hacer clic en un botón "Cerrar"
        boton_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        boton_cerrar.pack()

    def ocultar(self):
        # Esta función oculta la ventana de la página de inicio
        # se puede usar cuando el usuario inicia sesión correctamente y navega a otra sección de la aplicación
        self.withdraw()

# Ejemplo para mostrar la ventana de inicio
if __name__ == "__main__":
    ventana_inicio = VistaInicio()
    ventana_inicio.mainloop()
