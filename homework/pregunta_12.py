"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    archivo = open('files\input\data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t") for z in archivo]

    letras = sorted({fila[0] for fila in archivo})
    col5 = [[col[0],col[4].split(",")] for col in archivo]

    for fila in col5:
        for elemento in range(len(fila[1])):
            fila[1][elemento] = int(fila[1][elemento][4:])
        fila[1] = sum(fila[1])
    
    dicc = {letra: 0 for letra in letras}

    for elemento in col5:
        dicc[elemento[0]] += elemento[1]

    return dicc 

