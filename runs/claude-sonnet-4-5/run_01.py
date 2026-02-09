
import math

def min_odd_ticks(X, K):
    if X == 0:
        return 0
    k_odd = (K + 1) // 2
    if k_odd * k_odd >= X:
        # Find minimum m such that m^2 >= X
        m = int(math.sqrt(X))
        if m * m < X:
            m += 1
        return m
    else:
        # We need more than k_odd odd ticks
        remaining = X - k_odd * k_odd
        return k_odd + (remaining + K - 1) // K

def min_even_ticks(Y, K):
    if Y == 0:
        return 0
    k_even = K // 2
    if k_even * (k_even + 1) >= Y:
        # Find minimum m such that m * (m + 1) >= Y
        m = int(math.sqrt(Y))
        while m * (m + 1) < Y:
            m += 1
        return m
    else:
        # We need more than k_even even ticks
        remaining = Y - k_even * (k_even + 1)
        return k_even + (remaining + K - 1) // K

def solve(X, Y, K):
    if X == 0 and Y == 0:
        return 0
    
    m_x = min_odd_ticks(X, K)
    m_y = min_even_ticks(Y, K)
    
    if X == 0:
        return 2 * m_y
    elif Y == 0:
        return 2 * m_x - 1
    else:
        return max(2 * m_x - 1, 2 * m_y)

t = int(input())
for _ in range(t):
    X, Y, K = map(int, input().split())
    print(solve(X, Y, K))
