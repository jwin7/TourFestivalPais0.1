
from tkinter import Tk
from views.vista_inicio import VistaInicio

def main():
    root = Tk()
    app = VistaInicio(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
