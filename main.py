
from tkinter import Tk
from views.vista_inicio import VentanaInicio

if __name__ == "__main__":
    root = Tk()
    root.title("App de Eventos")
    root.geometry("400x300")

    ventana_inicio = VentanaInicio(root)

    root.mainloop()
