# def dominate(selected, graph, dominateds):
#     for dominated in graph[selected]:
#         dominateds.add(dominated)
#         for neighbor in graph[dominated]:
#             if dominated in graph[neighbor]:
#                 graph[neighbor].remove(dominated)
#         graph[dominated] = set()
#     graph[selected] = set()


# def greedy_dominating_set_o(graph):
#     graph = [set([neighbors]) for neighbors in graph]
#     dominateds = set()
#     answer = set()
#     while len(dominateds) < len(graph):
#         selected = max([(len(neighbors), i) for i, neighbors in enumerate(graph)])[1]
#         dominate(selected, graph, dominateds)
#         answer.add(selected)
#     return answer


# def dominate(selected, graph, dominateds):
#     to_remove = []  # Lista temporal para almacenar los elementos a modificar

#     for dominated in graph[selected]:
#         dominateds.add(dominated)
#         for neighbor in graph[dominated]:
#             if dominated in graph[neighbor]:
#                 to_remove.append(
#                     (neighbor, dominated)
#                 )  # Añadir a la lista temporal lo que se eliminará

#     # Ahora aplicar las modificaciones fuera del bucle
#     for neighbor, dominated in to_remove:
#         graph[neighbor].remove(dominated)

#     # Limpiar los conjuntos de dominados
#     graph[selected] = set()
#     for dominated in graph[selected]:
#         graph[dominated] = set()


# def greedy_dominating_set_o(graph):
#     # Convertir cada lista de vecinos en un conjunto
#     graph = [
#         set(graph[neighbors]) for neighbors in graph
#     ]  # Se quita la doble lista [set([neighbors])] para evitar error
#     dominateds = set()
#     answer = set()

#     while len(dominateds) < len(graph):
#         # Seleccionar el nodo con más vecinos no dominados
#         selected = max([(len(neighbors), i) for i, neighbors in enumerate(graph)])[1]
#         dominate(selected, graph, dominateds)
#         answer.add(selected)

#     return answer


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


def greedy_dominating_set_o(graph):
    # Convertir cada lista de vecinos en un conjunto para manipulación eficiente
    graph = {node: set(neighbors) for node, neighbors in graph.items()}
    dominateds = set()  # Nodos dominados
    answer = set()  # Conjunto dominante aproximado

    while len(dominateds) < len(graph):
        # Seleccionar el nodo con más vecinos no dominados
        selected = max(
            [
                (len(neighbors), node)
                for node, neighbors in graph.items()
                # if node not in dominateds
            ]
        )[1]

        # Dominar el nodo seleccionado y actualizar el grafo
        dominate(selected, graph, dominateds)
        answer.add(selected)

    return answer
