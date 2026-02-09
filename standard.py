"""
Reference solution for the alternating-axis movement problem.

For each test case (X, Y, K), compute the minimum number of ticks needed to
reach exactly (X, Y), where odd ticks add to X, even ticks add to Y, and on
tick i the added distance d satisfies 0 <= d <= min(K, i).
"""
import sys


def compute_max_x_distance(tick_count: int, limit_k: int) -> int:
    """
    Compute the maximum X distance achievable within the first tick_count ticks.

    Args:
        tick_count: Total number of ticks available.
        limit_k: Global cap K on the per-tick movement.

    Returns:
        The maximum possible total increase in X after tick_count ticks.
    """
    odd_tick_count = (tick_count + 1) // 2
    warm_odd_count = (limit_k + 1) // 2
    warm_used = min(odd_tick_count, warm_odd_count)

    warm_sum = warm_used * warm_used
    capped_sum = (odd_tick_count - warm_used) * limit_k
    return warm_sum + capped_sum


def compute_max_y_distance(tick_count: int, limit_k: int) -> int:
    """
    Compute the maximum Y distance achievable within the first tick_count ticks.

    Args:
        tick_count: Total number of ticks available.
        limit_k: Global cap K on the per-tick movement.

    Returns:
        The maximum possible total increase in Y after tick_count ticks.
    """
    even_tick_count = tick_count // 2
    warm_even_count = limit_k // 2
    warm_used = min(even_tick_count, warm_even_count)

    warm_sum = warm_used * (warm_used + 1)
    capped_sum = (even_tick_count - warm_used) * limit_k
    return warm_sum + capped_sum


def is_reachable_in_ticks(
    tick_count: int,
    target_x: int,
    target_y: int,
    limit_k: int,
) -> bool:
    """
    Check whether (target_x, target_y) is reachable in at most tick_count ticks.

    Args:
        tick_count: Candidate number of ticks.
        target_x: Required final X coordinate.
        target_y: Required final Y coordinate.
        limit_k: Global cap K on the per-tick movement.

    Returns:
        True if the target is reachable within tick_count ticks, otherwise False.
    """
    max_x_distance = compute_max_x_distance(tick_count, limit_k)
    max_y_distance = compute_max_y_distance(tick_count, limit_k)
    return max_x_distance >= target_x and max_y_distance >= target_y


def find_minimum_ticks(target_x: int, target_y: int, limit_k: int) -> int:
    """
    Find the minimum number of ticks required to reach exactly (target_x, target_y).

    Args:
        target_x: Required final X coordinate.
        target_y: Required final Y coordinate.
        limit_k: Global cap K on the per-tick movement.

    Returns:
        The minimum tick count needed.
    """
    if target_x == 0 and target_y == 0:
        return 0

    lower_bound_ticks = 0
    upper_bound_ticks = 1
    while not is_reachable_in_ticks(
        upper_bound_ticks,
        target_x,
        target_y,
        limit_k,
    ):
        upper_bound_ticks <<= 1

    while lower_bound_ticks + 1 < upper_bound_ticks:
        middle_ticks = lower_bound_ticks + (
            (upper_bound_ticks - lower_bound_ticks) // 2
        )
        if is_reachable_in_ticks(middle_ticks, target_x, target_y, limit_k):
            upper_bound_ticks = middle_ticks
        else:
            lower_bound_ticks = middle_ticks

    return upper_bound_ticks


def main() -> None:
    """
    Read input, solve all test cases, and write the results.

    Input format:
        t
        X Y K
        X Y K
        ...

    Output format:
        One line per test case: the minimum required ticks.
    """
    input_stream = sys.stdin.buffer
    first_line = input_stream.readline().split()
    test_case_count = int(first_line[0])

    output_lines = []
    for _ in range(test_case_count):
        target_x_str, target_y_str, limit_k_str = input_stream.readline().split()
        target_x = int(target_x_str)
        target_y = int(target_y_str)
        limit_k = int(limit_k_str)

        answer_ticks = find_minimum_ticks(target_x, target_y, limit_k)
        output_lines.append(str(answer_ticks))

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()