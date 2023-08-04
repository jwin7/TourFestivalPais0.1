import tkinter as tk


def mostrar_vista_login():
    # Crea la ventana y los elementos de la vista para la página de inicio de sesión
    ventana = tk.Tk()
    ventana.title("Inicio de Sesión")

    # Agrega elementos de la página de inicio de sesión, como campos de entrada para usuario y contraseña, etc.

    # Ejemplo para cerrar la ventana al hacer clic en un botón "Cerrar"
    boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack()

def mostrar_mensaje_error(mensaje):
    # Esta función muestra un mensaje de error en la vista de inicio de sesión
    # Puedes usarla para mostrar mensajes de error cuando las credenciales ingresadas son incorrectas
    tk.messagebox.showerror("Error", mensaje)

