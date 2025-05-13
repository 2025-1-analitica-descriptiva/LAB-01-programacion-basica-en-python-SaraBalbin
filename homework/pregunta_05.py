"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    archivo = open('files\input\data.csv', 'r').readlines()
    archivo = [z.replace("\n", "").split("\t") for z in archivo]

    letras = sorted({fila[0] for fila in archivo})
    letraNumero = [(fila[0], int(fila[1])) for fila in archivo]

    minmax = {letra: [] for letra in letras}
    for i in letraNumero:
        minmax[i[0]].append(i[1])
    
    x = []
    for i in minmax:
        x.append((i, max(minmax[i]), min(minmax[i])))

    return x