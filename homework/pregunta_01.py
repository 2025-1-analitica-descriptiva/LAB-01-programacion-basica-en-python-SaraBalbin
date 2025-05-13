"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    archivo = open('files/input/data.csv', 'r').readlines()
    archivo = [z.replace("\n", "").split("\t") for z in archivo]
    suma = [int(fila[1]) for fila in archivo]
    return sum(suma)

print(pregunta_01())