import models.eventos as modelo_eventos
import views.vista_explorar as vista_explorar
from views.vista_resultados import VistaResultados

def buscar_eventos_por_nombre(nombre):
    eventos = modelo_eventos.cargar_eventos()
    eventos_encontrados = [evento for evento in eventos if nombre.lower() in evento.nombre.lower()]
    vista_explorar.mostrar_resultados(eventos_encontrados)

def buscar_eventos_por_genero(genero):
    eventos = modelo_eventos.cargar_eventos()
    eventos_encontrados = [evento for evento in eventos if genero.lower() in evento.genero.lower()]
    vista_explorar.mostrar_resultados(eventos_encontrados)

def buscar_eventos_por_artista(artista):
    eventos = modelo_eventos.cargar_eventos()
    eventos_encontrados = [evento for evento in eventos if artista.lower() in evento.artista.lower()]
    vista_explorar.mostrar_resultados(eventos_encontrados)

def filtrar_eventos_por_ubicacion(ubicacion_id):
    eventos = modelo_eventos.cargar_eventos()
    eventos_filtrados = [evento for evento in eventos if evento.id_ubicacion == ubicacion_id]
    vista_explorar.mostrar_resultados(eventos_filtrados)

def filtrar_eventos_por_horario(hora_inicio, hora_fin):
    eventos = modelo_eventos.cargar_eventos()
    eventos_filtrados = [evento for evento in eventos if hora_inicio <= evento.hora_inicio <= hora_fin]
    vista_explorar.mostrar_resultados(eventos_filtrados)

def mostrar_explorar():
    ventana_explorar = vista_explorar.VistaExplorar()
    ventana_explorar.mainloop()

def ocultar_explorar():
    ventana_explorar.ocultar()    
      
