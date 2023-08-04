import tkinter as tk
import json
import views.vista_login as vista_login
from controllers.controlador_inicio import mostrar_inicio

def verificar_credenciales(usuario, contrasena):
    # Leer el archivo de usuarios (usuario.json)
    with open('data/usuarios.json', 'r') as file:
        usuarios = json.load(file)

    # Buscar el usuario en la lista de usuarios
    for user in usuarios["usuarios"]:
        if user["nombre"] == usuario and user["contrasena"] == contrasena:
            # Si se encuentra el usuario y la contraseña es correcta, obtener el usuario_id
            usuario_id = user["id"]

            # Mostrar la vista de inicio con el usuario_id
            vista_login.ocultar_vista()
            controlador_inicio.mostrar_inicio(usuario_id)  # Asegúrate de importar controlador_inicio

            return

    # Si las credenciales son incorrectas, mostrar un mensaje de error en la vista de login
    vista_login.mostrar_mensaje_error("Credenciales incorrectas. Inténtalo nuevamente.")
