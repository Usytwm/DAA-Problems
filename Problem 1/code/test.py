from pathlib import Path
import random
import sys
import time

# path_to_root = Path(__file__).resolve().parents[0]
# sys.path.append(str(path_to_root))

from optimized_solution import expected_value_optimized
from solution import expected_value


def test_performance():
    test_cases = [
        [10**6] * 10**5,  # large input all same
        [random.randint(1, 10**6) for _ in range(10**5)],  # large input random values
        list(range(10**5, 0, -1)),  # descending sorted
        [10**9] * 10**5,  # extremely large values
        [10**9 if i % 2 == 0 else 1 for i in range(10**5)],  # alternating high low
    ]

    for index, c in enumerate(test_cases, start=1):
        print(f"Testing case {index} with {len(c)} elements.")
        # Test optimized version
        start_time = time.time()
        result_optimized = expected_value_optimized(c.copy())
        end_time = time.time()
        print(f"Optimized version took {end_time - start_time:.2f} seconds.")

        # Test normal version
        start_time = time.time()
        result_normal = expected_value(c.copy())
        end_time = time.time()
        print(f"Normal version took {end_time - start_time:.2f} seconds.")

        # Verify results are the same
        assert result_optimized == result_normal, "Results differ between versions!"
        print("Results are identical between both versions.\n")


if __name__ == "__main__":
    test_performance()
