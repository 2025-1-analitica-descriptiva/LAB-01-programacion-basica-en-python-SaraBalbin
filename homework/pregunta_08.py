"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    archivo = open('files\input\data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    columnas = [(fila[0], int(fila[1])) for fila in archivo]
    numeros = sorted([fila[1] for fila in columnas])
    numeros = {numero: [] for numero in numeros}

    for i in columnas:
        if i[0] not in numeros[i[1]]:
            numeros[i[1]].append(i[0])

    x = []
    for j in numeros:
        x.append((j, sorted(numeros[j])))

    return x

