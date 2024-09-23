import random


def generate_random_graph(num_nodos, probabilidad_conexion=0.5):
    """
    Genera un grafo aleatorio utilizando un número de nodos y una probabilidad de conexión.
    ---
    :param num_nodos: Número de nodos en el grafo.
    :param probabilidad_conexion: Probabilidad de que dos nodos estén conectados.
    :return: Un diccionario que representa el grafo.
    """
    grafo = {i: [] for i in range(num_nodos)}

    for i in range(num_nodos):
        for j in range(i + 1, num_nodos):
            if random.random() < probabilidad_conexion:
                # (grafo no dirigido)
                grafo[i].append(j)
                grafo[j].append(i)

    return grafo
