
def build_input(cases):
    return str(len(cases)) + "\n" + "\n".join(f"{x} {y} {k}" for x, y, k in cases)

inputs = []

# Input 1: (0,0) special case => answer must be 0
inputs.append(build_input([(0, 0, 1)]))

# Input 2: X=0, small Y; must "wait" on odd ticks (d=0) and move only on even ticks
inputs.append(build_input([(0, 5, 10)]))

# Input 3: Y=0, small X; must "wait" on even ticks (d=0) and move only on odd ticks
inputs.append(build_input([(5, 0, 10)]))

# Input 4: Minimal nonzero Y with huge K; still cannot move north until tick 2
inputs.append(build_input([(0, 1, 10**9)]))

# Input 5: Minimal nonzero X with huge K; can move east immediately on tick 1
inputs.append(build_input([(1, 0, 10**9)]))

# Input 6: Exact-capacity boundary around K=3 at n=3 (odd ticks 1 and 3 => 1+3=4, even tick 2 =>2)
inputs.append(build_input([(4, 2, 3)]))

# Input 7: Just-over boundary for X with K=3; forces extra odd ticks past the breakpoint
inputs.append(build_input([(5, 2, 3)]))

# Input 8: Exact-capacity boundary around K=4 at n=4 (odds 1+3=4, evens 2+4=6)
inputs.append(build_input([(4, 6, 4)]))

# Input 9: Just-over boundary for Y with K=4; forces more even ticks
inputs.append(build_input([(4, 7, 4)]))

# Input 10: K=1 worst-case huge X only; n can be ~2*X-1 (very large), stresses upper bound + overflow
inputs.append(build_input([(10**18, 0, 1)]))

# Input 11: K=1 worst-case huge Y only; requires n ~ 2*Y (very large)
inputs.append(build_input([(0, 10**18, 1)]))

# Input 12: K=1 huge both; extremely large minimal n, stresses performance and 128-bit arithmetic in solutions
inputs.append(build_input([(10**18, 10**18, 1)]))

# Input 13: Small K=2 case that hits saturation quickly; exact boundary (n=3 gives X cap 1+2=3, Y cap 2)
inputs.append(build_input([(3, 2, 2)]))

# Input 14: Skewed distribution: enormous X, tiny Y with large K; checks parity handling and independence
inputs.append(build_input([(10**18, 1, 10**9)]))

# Input 15: Multi-test stress (t=100): mixed K regimes, parities, zeros, and a few extremes
cases15 = []
for i in range(1, 98):
    x = i * i                  # up to 97^2 = 9409
    y = (i * 37) % 123         # small-ish, includes 0
    k = 1 if i % 11 == 0 else (i % 9) + 1  # range 1..10 (incl. K=1 sometimes)
    cases15.append((x, y, k))

# Add a few heavy extremes at the end (still within constraints)
cases15.append((0, 0, 999_999_937))         # origin with large prime-ish K (<= 1e9)
cases15.append((10**18, 10**18, 2))         # huge both with small K>1
cases15.append((10**18, 0, 10**9))          # huge X only with max K
inputs.append(build_input(cases15))

print("Test Cases:")
for idx, s in enumerate(inputs, 1):
    print(f"Input {idx}:")
    print(s)
    if idx != len(inputs):
        print()
