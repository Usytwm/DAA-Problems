import heapq
import random


def generate_random_graph(num_nodos, probabilidad_conexion):
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


def greedy_dominating_set(graph):
    """
    Implementa el algoritmo greedy para encontrar un conjunto dominante aproximado en un grafo.
    ---
    :param graph: Un diccionario que representa el grafo, donde las llaves son los nodos y los valores son listas de vecinos.
    :return: Un conjunto dominante aproximado.
    """
    dominated = set()  # Conjunto de vértices ya dominados
    dominating_set = set()  # Conjunto que contiene la solución aproximada

    heap = [(-len(neighbors), vertex) for vertex, neighbors in graph.items()]
    # Convertir la lista en un heap en O(n)
    heapq.heapify(heap)

    while len(dominated) < len(graph):
        # Sacar el vértice que domina más nodos no dominados
        _, best_vertex = heapq.heappop(heap)
        if best_vertex not in dominated:
            # Añadir el vértice al conjunto dominante
            dominating_set.add(best_vertex)
            # Marcar como dominados el vértice y sus vecinos
            dominated.add(best_vertex)
            for neighbor in graph[best_vertex]:
                dominated.add(neighbor)

    return dominating_set


def test_greedy_dominating_set(num_nodos, probabilidad_conexion):
    grafo = generate_random_graph(num_nodos, probabilidad_conexion)
    dominating_set = greedy_dominating_set(grafo)
    return dominating_set


dominating_set = test_greedy_dominating_set(1024, 0.3)

print(f"Conjunto dominante aproximado: {dominating_set}")
