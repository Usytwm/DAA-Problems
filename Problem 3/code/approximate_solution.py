def greedy_dominating_set(graph):
    """
    Implementa el algoritmo greedy ajustado para encontrar un conjunto dominante aproximado en un grafo,
    seleccionando el nodo con más vecinos no dominados en cada paso.
    ---

    :param graph: Un diccionario que representa el grafo, donde las llaves son los nodos y los valores son listas de vecinos.
    :return: Un conjunto dominante aproximado.
    """
    dominated = set()  # Conjunto de vértices ya dominados
    dominating_set = set()  # Conjunto que contiene la solución aproximada

    while len(dominated) < len(graph):
        # Buscar el nodo que domina más vecinos no dominados
        best_vertex = None
        max_undominated_neighbors = -1

        for vertex in graph:
            if vertex not in dominated:
                # Contar cuántos vecinos no dominados tiene este nodo, incluyéndolo si no está dominado
                undominated_neighbors = [
                    neighbor for neighbor in graph[vertex] if neighbor not in dominated
                ]
                if len(undominated_neighbors) > max_undominated_neighbors:
                    max_undominated_neighbors = len(undominated_neighbors)
                    best_vertex = vertex

        # Añadir el mejor nodo al conjunto dominante
        dominating_set.add(best_vertex)
        # Marcar como dominado el nodo y sus vecinos no dominados
        dominated.add(best_vertex)
        for neighbor in graph[best_vertex]:
            dominated.add(neighbor)

    return dominating_set
