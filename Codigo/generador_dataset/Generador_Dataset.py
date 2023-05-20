from generador_dataset.generador import figurasGeometricas


def generarFiguras(tamanio, destino, animacion):
    generador = figurasGeometricas(
        tamanio=tamanio, destino=destino, animacion=animacion
    )
    generador.generar()
