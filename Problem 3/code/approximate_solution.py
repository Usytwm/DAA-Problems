def dominate(selected, graph, dominateds):
    # Agregar el nodo seleccionado y sus vecinos al conjunto de dominados
    dominateds.add(selected)
    for dominated in graph[selected]:
        dominateds.add(dominated)

    # Actualizar las listas de adyacencia de todos los nodos eliminando los dominados
    for node in graph:
        graph[node] = [
            neighbor for neighbor in graph[node] if neighbor not in dominateds
        ]


def greedy_dominating_set(graph):
    # Convertir cada lista de vecinos en un conjunto para manipulación eficiente
    graph = {node: set(neighbors) for node, neighbors in graph.items()}
    dominateds = set()  # Nodos dominados
    answer = set()  # Conjunto dominante aproximado

    # Dominar los nodos sin vecinos
    for node in graph:
        if len(graph[node]) == 0:
            answer.add(node)
            dominateds.add(node)

    while len(dominateds) < len(graph):
        # Seleccionar el nodo con más vecinos no dominados
        selected = max([(len(neighbors), node) for node, neighbors in graph.items()])[1]

        # Dominar el nodo seleccionado y actualizar el grafo
        dominate(selected, graph, dominateds)
        answer.add(selected)

    return answer
