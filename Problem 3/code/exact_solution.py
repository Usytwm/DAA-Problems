import itertools


def is_dominating_set(graph, candidate_set):
    """
    Verifica si el conjunto candidato es un conjunto dominante para el grafo.
    ---
    :param graph: Un diccionario que representa el grafo.
    :param candidate_set: Conjunto candidato para ser evaluado.
    :return: True si el conjunto candidato es dominante, False en caso contrario.
    """
    dominated = set(candidate_set)
    for node in candidate_set:
        dominated.update(
            graph[node]
        )  # Añadir los vecinos del nodo al conjunto dominado
    return len(dominated) == len(graph)


def find_minimum_dominating_set(graph):
    """
    Encuentra el conjunto dominante mínimo utilizando una búsqueda por tamaño creciente de subconjuntos.
    ---
    :param graph: Un diccionario que representa el grafo.
    :return: El conjunto dominante mínimo encontrado.
    """
    nodes = list(graph.keys())

    # Probar subconjuntos de tamaño creciente, desde 1 hasta len(nodes)
    for size in range(1, len(nodes) + 1):
        # Generar todos los subconjuntos de tamaño 'size'
        for subset in itertools.combinations(nodes, size):
            if is_dominating_set(graph, subset):
                return list(
                    subset
                )  # Retornar la primera solución encontrada (que será la mínima)

    return nodes  # En el peor caso, retornar todos los nodos (caso donde todo el grafo es el conjunto dominante)


graph = {
    "A": ["B", "H"],
    "B": ["A", "C", "H"],
    "C": ["B", "D", "E", "F", "H"],
    "D": ["C", "F", "G"],
    "E": ["C", "F"],
    "F": ["C", "D", "E", "G"],
    "G": ["D", "F", "H"],
    "H": ["A", "B", "C", "G"],
}

minimum_dominating_set = find_minimum_dominating_set(graph)
print(f"Conjunto dominante mínimo: {minimum_dominating_set}")
