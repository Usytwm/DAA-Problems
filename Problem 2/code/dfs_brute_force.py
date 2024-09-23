pass  # No Terminado AUNN


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


def split(points):
    points_by_row = {}
    points_by_column = {}
    for i, (row, column) in enumerate(points):
        if not row in points_by_row:
            points_by_row[row] = []
        points_by_row[row].append(i)
        if not column in points_by_column:
            points_by_column[column] = []
        points_by_column[column].append(i)
    return points_by_row, points_by_column


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
    return points, len(rows), len(columns)


def fullfills(tpl, points, points_by_row, points_by_column, n_rows):
    covered_points = set()
    for x in tpl:
        if x < n_rows:
            for id in points_by_row[x]:
                covered_points.add(id)
        else:
            for id in points_by_column[x - n_rows]:
                covered_points.add(id)
        if len(covered_points) == len(points):
            return True
    return False


def count_turned_on_bits(n):
    return bin(n).count("1")


def DFS(x, visited, n_bits, points_by_row, points_by_column):
    visited.add(x)
    answer = -1
    for i in range(n_bits):
        next = x & ((1 << n_bits - 1) - (1 << i))
        if (
            (next != x)
            and (not next in visited)
            and fullfills(next, points_by_row, points_by_column, n_bits)
        ):
            answer = max(
                answer, DFS(next, visited, n_bits, points_by_row, points_by_column)
            )
    if answer == -1:
        return count_turned_on_bits(x)
    return answer


def main():
    _, _, sections = read_data()
    points, n_rows, n_columns = extract_data(sections)
    points_by_row, points_by_column = split(points)
    n_bits = n_rows + n_columns
    print(DFS(1 << n_bits - 1, set(), n_bits, points_by_row, points_by_column))


main()
