"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    archivo = open('files/input/data.csv', 'r').readlines()
    archivo = [z.replace("\n", "").split("\t") for z in archivo]
    letrasNumeros = [(fila[0], int(fila[1])) for fila in archivo]
    letrasSuma = {fila[0]:0 for fila in archivo}
    for i in letrasNumeros:
        if i[0] in letrasSuma.keys():
            letrasSuma[i[0]] += i[1]
   
    final = sorted(letrasSuma.items())
    return final
