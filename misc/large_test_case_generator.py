
# Generates 10 large input examples for the "Alternating Rails" problem.
# Prints them in the exact requested format.

def sum_odds_upto(n: int) -> int:
    # Sum of odd integers <= n
    # If n=2m or 2m-1, odds are 1..(2m-1): sum = m^2
    m = (n + 1) // 2
    return m * m

def sum_evens_upto(n: int) -> int:
    # Sum of even integers <= n
    # If n=2m: 2+4+...+2m = m(m+1)
    # If n=2m-1: 2+...+2(m-1) = (m-1)m
    m = n // 2
    return m * (m + 1)

def build_inputs():
    inputs = []

    # 1) Max X,Y with minimal K (worst-case huge tick count; linear growth)
    inputs.append(f"1\n{10**18} {10**18} 1\n")

    # 2) Max X,Y with maximal K (quadratic early regime; big arithmetic)
    inputs.append(f"1\n{10**18} {10**18} {10**9}\n")

    # 3) X huge, Y=0, small K (must use many zero moves on even ticks)
    inputs.append(f"1\n{10**18} 0 1\n")

    # 4) Y huge, X=0, small K (must use many zero moves on odd ticks)
    inputs.append(f"1\n0 {10**18} 1\n")

    # 5) Boundary at n=K with K even: choose (X,Y) exactly at capacities for n=K
    K_even = 10**9  # even
    X5 = sum_odds_upto(K_even)
    Y5 = sum_evens_upto(K_even)
    inputs.append(f"1\n{X5} {Y5} {K_even}\n")

    # 6) Just-over boundary (force n > K): X = capX(K)+1, Y = capY(K)
    inputs.append(f"1\n{X5 + 1} {Y5} {K_even}\n")

    # 7) Boundary at n=K with K odd: tick K contributes to X (odd tick)
    K_odd = 999_999_999
    X7 = sum_odds_upto(K_odd)
    Y7 = sum_evens_upto(K_odd)
    inputs.append(f"1\n{X7} {Y7} {K_odd}\n")

    # 8) Highly skewed: X huge, Y tiny, small K (parity + tail behavior)
    inputs.append(f"1\n{10**18} 1 2\n")

    # 9) Highly skewed: Y huge, X tiny, small K (parity + tail behavior)
    inputs.append(f"1\n1 {10**18} 2\n")

    # 10) Stress: very large t with mixed K regimes and large coordinates
    t = 10_000
    lines = [str(t)]
    for j in range(t):
        r = j % 4
        if r == 0:
            K = 1
        elif r == 1:
            K = 2
        elif r == 2:
            K = 10**9
        else:
            K = 999_999_937  # large prime near 1e9

        # Keep X,Y large and varying; always within [0, 1e18]
        X = 10**18 - 123_456 * (j + 1)
        Y = 10**18 - 789_012 * (j + 1)

        if X < 0:
            X = 0
        if Y < 0:
            Y = 0

        lines.append(f"{X} {Y} {K}")
    inputs.append("\n".join(lines) + "\n")

    return inputs

def main():
    inputs = build_inputs()
    print("**Test Cases: **")
    for i, s in enumerate(inputs, 1):
        print(f"Input {i}:")
        print(s, end="" if s.endswith("\n") else "\n")
        if i != len(inputs):
            print()

if __name__ == "__main__":
    main()
