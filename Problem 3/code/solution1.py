import heapq


def greedy_dominating_set(graph):
    """
    Implementa el algoritmo greedy para encontrar un conjunto dominante aproximado en un grafo.
    :param graph: Un diccionario que representa el grafo, donde las llaves son los nodos y los valores son listas de vecinos.
    :return: Un conjunto dominante aproximado.
    """
    dominated = set()  # Conjunto de vértices ya dominados
    dominating_set = set()  # Conjunto que contiene la solución aproximada
    heap = []

    # Inicializar un heap donde guardamos el grado de dominación de cada vértice
    for vertex, neighbors in graph.items():
        heapq.heappush(
            heap, (-len(neighbors), vertex)
        )  # Guardamos el negativo del grado para tener un max-heap

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


# Ejemplo de uso:
graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4, 5], 4: [3], 5: [3]}

dominant_set = greedy_dominating_set(graph)
print(f"Conjunto dominante aproximado: {dominant_set}")


def greedy_dominating_set(graph):
    """
    Implementa el algoritmo greedy para encontrar un conjunto dominante aproximado en un grafo.
    :param graph: Un diccionario que representa el grafo, donde las llaves son los nodos y los valores son listas de vecinos.
    :return: Un conjunto dominante aproximado.
    """
    # Inicializar el conjunto de vértices dominados (vacío al principio)
    dominated = set()
    # Conjunto dominante
    dominating_set = set()

    # Mientras haya vértices no dominados
    while len(dominated) < len(graph):
        # Seleccionamos el vértice que domine más nodos no dominados
        best_vertex = None
        max_dominates = -1

        for vertex in graph:
            if vertex not in dominating_set:
                # Contamos cuántos vértices no dominados domina este vértice
                dominates = {
                    neighbor for neighbor in graph[vertex] if neighbor not in dominated
                }
                if vertex not in dominated:
                    dominates.add(
                        vertex
                    )  # Contamos el propio vértice si tampoco está dominado

                # Comparamos con el máximo actual
                if len(dominates) > max_dominates:
                    max_dominates = len(dominates)
                    best_vertex = vertex

        # Añadir el mejor vértice al conjunto dominante
        dominating_set.add(best_vertex)
        # Marcar todos los vecinos del vértice (y el propio vértice) como dominados
        dominated.add(best_vertex)
        dominated.update(graph[best_vertex])

    return dominating_set


# Ejemplo de uso:
graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4, 5], 4: [3], 5: [3]}

dominant_set = greedy_dominating_set(graph)
print(f"Conjunto dominante aproximado: {dominant_set}")


import heapq


def greedy_dominating_set_optimized(graph):
    """
    Implementa el algoritmo greedy mejorado usando una cola de prioridad para encontrar un conjunto dominante aproximado.
    :param graph: Un diccionario que representa el grafo, donde las llaves son los nodos y los valores son listas de vecinos.
    :return: Un conjunto dominante aproximado.
    """
    # Inicializar el conjunto de vértices dominados (vacío al principio)
    dominated = set()
    # Conjunto dominante
    dominating_set = set()

    # Inicializar el heap para la cola de prioridad, donde almacenamos (vecinos no dominados, vértice)
    heap = []
    vertex_dominated_count = {
        v: len(graph[v]) for v in graph
    }  # número de vecinos no dominados por vértice

    # Inicializamos la cola de prioridad
    for vertex, count in vertex_dominated_count.items():
        heapq.heappush(heap, (-count, vertex))  # Negamos el valor para que sea max-heap

    # Mientras haya vértices no dominados
    while len(dominated) < len(graph):
        # Sacar el vértice con mayor número de vecinos no dominados
        while heap:
            count, best_vertex = heapq.heappop(heap)
            count = -count  # revertir el signo
            if best_vertex not in dominated:
                break

        # Añadir el mejor vértice al conjunto dominante
        dominating_set.add(best_vertex)
        # Marcar todos sus vecinos y el propio vértice como dominados
        dominated.add(best_vertex)
        for neighbor in graph[best_vertex]:
            dominated.add(neighbor)

        # Actualizamos los vecinos no dominados de los vértices restantes
        for neighbor in graph[best_vertex]:
            if neighbor not in dominating_set:
                vertex_dominated_count[neighbor] = len(
                    [n for n in graph[neighbor] if n not in dominated]
                )
                heapq.heappush(heap, (-vertex_dominated_count[neighbor], neighbor))

    return dominating_set


# Ejemplo de uso:
graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3], 3: [1, 2, 4, 5], 4: [3], 5: [3]}

dominant_set = greedy_dominating_set_optimized(graph)
print(f"Conjunto dominante aproximado: {dominant_set}")
