from collections import deque

INF = (1 << 64) - 1


def read_data():
    n, k = [int(x) for x in input().split()]
    sections = []
    for _ in range(k):
        sections.append(tuple([int(x) for x in input().split()]))
    return n, k, sections


def all_points(section):
    x1, y1, x2, y2 = section
    points = []
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            points.append((x, y))
    return points


def extract_data(sections):
    rows = {}
    columns = {}
    points = []
    for section in sections:
        for row, column in all_points(section):
            if not row in rows:
                rows[row] = len(rows)
            if not column in columns:
                columns[column] = len(columns)
            points.append((row, column))
    points = [(rows[row], columns[column]) for row, column in points]
    return points, rows, columns


def build_graph(points, n_rows, n_columns):
    total_vertices = n_rows + n_columns + 2
    graph = [[0 for _ in range(total_vertices)] for _ in range(total_vertices)]
    source = total_vertices - 2
    sink = total_vertices - 1
    for row, column in points:
        column += n_rows
        graph[row][column] = INF
    for i in range(n_rows):
        graph[source][i] = 1
    for i in range(n_columns):
        graph[n_rows + i][sink] = 1
    return graph


def BFS(graph, parents):
    source = len(graph) - 2
    sink = len(graph) - 1
    visited = [False] * len(parents)
    queue = deque([source])
    visited[source] = True
    while queue:
        u = queue.popleft()
        for ind, cap in enumerate(graph[u]):
            if visited[ind] == False and cap > 0:
                queue.append(ind)
                visited[ind] = True
                parents[ind] = u
                if ind == sink:
                    return True
    return False


def Edmonds_Karp(graph):
    parents = [-1] * len(graph)
    max_flow = 0
    source = len(graph) - 2
    sink = len(graph) - 1
    while BFS(graph, parents):
        path_flow = INF
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parents[s]][s])
            s = parents[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parents[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parents[v]

    return max_flow


def main(sections=None):
    if sections is None:
        _, _, sections = read_data()
    points, rows, columns = extract_data(sections)
    graph = build_graph(points, len(rows), len(columns))
    return Edmonds_Karp(graph)


main()
