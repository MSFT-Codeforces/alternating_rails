
def main():
    inputs = []

    # 1) Minimum boundary: origin special-case
    inputs.append("1\n0 0 1\n")

    # 2) Only X positive (requires only odd ticks; must waste even ticks with d=0)
    #    Also exercises i<K ramp (K=2): tick1 cap=1, tick3 cap=2
    inputs.append("1\n2 0 2\n")

    # 3) Only Y positive (requires even ticks; must wait on tick 1)
    inputs.append("1\n0 6 2\n")

    # 4) Minimal answer should be 1 tick (odd tick moves east)
    inputs.append("1\n1 0 5\n")

    # 5) Minimal answer should be 2 ticks (need even tick to move north; tick 1 must be 0)
    inputs.append("1\n0 1 1\n")

    # 6) Boundary equality around K (K=3): capX at n=3 is 1+3=4
    inputs.append("1\n4 0 3\n")

    # 7) Just over boundary around K (K=3): X=5 forces extra odd tick
    inputs.append("1\n5 0 3\n")

    # 8) Even K boundary (K=4): capY at n=4 is 2+4=6
    inputs.append("1\n0 6 4\n")

    # 9) Just over even-K boundary (K=4): Y=7 forces extra even tick
    inputs.append("1\n0 7 4\n")

    # 10) K very large relative to needed ticks (min(K,i)=i), mixed X/Y
    inputs.append("1\n4 6 100\n")

    # 11) K=1 linear growth, mixed X/Y
    inputs.append("1\n3 4 1\n")

    # 12) Skewed: X large, Y tiny; forces many odd contributions and possibly wasted even ticks
    inputs.append("1\n10 1 2\n")

    # 13) Skewed opposite: X tiny, Y large
    inputs.append("1\n1 10 2\n")

    # 14) Same (X,Y) with different K to test piecewise/min(K,i) handling
    inputs.append("3\n2 2 1\n2 2 2\n2 2 3\n")

    # 15) Small multi-case mix: parity + around K transitions + zeros allowed
    inputs.append(
        "5\n"
        "0 0 7\n"
        "2 0 1\n"
        "0 2 1\n"
        "3 3 2\n"
        "6 1 3\n"
    )

    print("**Test Cases: **")
    for i, s in enumerate(inputs, 1):
        print(f"Input {i}:")
        print(s, end="")
        if not s.endswith("\n"):
            print()
        print()

if __name__ == "__main__":
    main()
