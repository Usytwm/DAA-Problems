import random
from brute_force import main as brute_force_main


def generate_random_test_case(n, m):
    sections = []
    for i in range(m):
        x1 = random.randint(1, n)
        y1 = random.randint(1, n)
        x2 = random.randint(x1, n)
        y2 = random.randint(y2, n)
        sections.append((x1, y1, x2, y2))
    return sections


def correctness_test(implementation, n, m):
    sections = generate_random_test_case(n, m)
    return implementation(sections) == brute_force_main(sections)


def speed_test(implementation, n, m):
    sections = generate_random_test_case(n, m)
    start_time = time.time()
    implementation(sections)
    end_time = time.time()
    return end_time - start_time
