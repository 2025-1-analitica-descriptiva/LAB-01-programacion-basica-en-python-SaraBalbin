"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    from collections import Counter
    archivo = open('files/input/data.csv', 'r').readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split("\t")[4].split(",") for z in archivo]
    letras = sorted(palabra[:3] for diccionario in archivo for palabra in diccionario)
    letras = dict(Counter(letras))
    return letras
