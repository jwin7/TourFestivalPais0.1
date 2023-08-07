from views.vista_inicio import VistaInicio
from views.vista_eventos import VistaEventos
from controllers.controlador_usuarios import ControladorUsuarios


def main():
    vista_inicio = VistaInicio()
    controlador_usuarios = ControladorUsuarios()

    # Llamar a la función mostrar_ventana_inicio() y almacenar el objeto VistaInicio en una variable
    ventana_inicio = vista_inicio.mostrar_ventana_inicio(controlador_usuarios)

    # Aquí puedes utilizar la variable ventana_inicio para acceder a métodos o atributos de la clase VistaInicio si es necesario

if __name__ == "__main__":
    main()
