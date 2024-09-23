from more_itertools import powerset


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
    return points, len(rows), len(columns)


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


def main():
    _, _, sections = read_data()
    points, n_rows, n_columns = extract_data(sections)
    points_by_row, points_by_column = split(points)
    for tpl in powerset([i for i in range(n_rows + n_columns)]):
        if fullfills(tpl, points, points_by_row, points_by_column, n_rows):
            print(len(tpl))
            return


main()
