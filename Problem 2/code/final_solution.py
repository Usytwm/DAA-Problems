from collections import deque

INF = (1 << 64) - 1


def read_data():
    n, k = [int(x) for x in input().split()]
    sections = []
    for _ in range(k):
        sections.append(tuple([int(x) for x in input().split()]))
    return n, k, sections


def prepare_ranges(sections, just_rows=True):
    borders = set()
    alias = {}
    widths = []
    if just_rows:
        sections = [(x1, x2) for x1, _, x2, _ in sections]
    else:
        sections = [(y1, y2) for _, y1, _, y2 in sections]
    for section_id, (op, cl) in enumerate(sections):
        alias[op] = None
        alias[cl] = None
        cl += 1
        borders.add(op)
        borders.add(cl)
    borders = list(borders)
    borders.sort()
    all_pos = list(set(borders + list(alias.keys())))
    all_pos.sort()
    current_range_start = None
    current_range_id = 0
    for pos in all_pos:
        if current_range_start is None:
            current_range_start = pos
            alias[pos] = current_range_id
            continue
        if pos in borders:
            widths.append(pos - current_range_start)
            current_range_start = pos
            current_range_id += 1
        if pos in alias:
            alias[pos] = current_range_id
    return alias, widths


def compress_data(sections):
    row_alias, row_widths = prepare_ranges(sections)
    column_alias, column_widths = prepare_ranges(sections, False)
    return (
        [
            (row_alias[x1], column_alias[y1], row_alias[x2], column_alias[y2])
            for x1, y1, x2, y2 in sections
        ],
        row_widths,
        column_widths,
    )


def all_points(section):
    x1, y1, x2, y2 = section
    points = []
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            points.append((x, y))
    return points


def build_graph(sections, row_widths, column_widths):
    total_vertices = len(row_widths) + len(column_widths) + 2
    graph = [[0 for _ in range(total_vertices)] for _ in range(total_vertices)]
    source = total_vertices - 2
    sink = total_vertices - 1
    n_rows = len(row_widths)
    for section in sections:
        for row, column in all_points(section):
            column += n_rows
            graph[row][column] = INF
    for i, width in enumerate(row_widths):
        graph[source][i] = width
    for i, width in enumerate(column_widths):
        graph[n_rows + i][sink] = width
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


def main():
    _, _, sections = read_data()
    sections, row_widths, column_widths = compress_data(sections)
    graph = build_graph(sections, row_widths, column_widths)
    print(Edmonds_Karp(graph))


main()
