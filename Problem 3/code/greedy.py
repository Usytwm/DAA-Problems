def dominate(selected, graph, dominateds):
    for dominated in graph[selected]:
        dominateds.add(dominated)
        for neighbor in graph[dominated]:
            if dominated in graph[neighbor]:
                graph[neighbor].remove(dominated)
        graph[dominated] = set()
    graph[selected] = set()


def greedy_dominating_set(graph):
    graph = [set(neighbors) for neighbors in graph]
    dominateds = set()
    answer = set()
    while len(dominateds) < len(graph):
        selected = max([(len(neighbors), i) for i, neighbors in graph])[1]
        dominate(selected, graph, dominateds)
        answer.add(selected)
    return answer
