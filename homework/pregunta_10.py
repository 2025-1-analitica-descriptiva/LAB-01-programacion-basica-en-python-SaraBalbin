"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    archivo = open('files/input/data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]
    columnas = [[col[0], col[3].split(","), col[4].split(",") ] for col in archivo]

    x = []
    for elemento in columnas:
        x.append((elemento[0], len(elemento[1]), len(elemento[2])))

    return x