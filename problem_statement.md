Time Limit: **2 seconds**

Memory Limit: **32 MB**

A robot starts at point $(0, 0)$ on an infinite 2D grid and must reach exactly $(X, Y)$.

Movement happens in discrete ticks $i = 1, 2, 3, \dots$:

- On **odd** ticks ($i = 1, 3, 5, \dots$), the robot may move only **east** (increase $X$).
- On **even** ticks ($i = 2, 4, 6, \dots$), the robot may move only **north** (increase $Y$).

On tick $i$, the robot chooses an integer distance $d$ such that
$$
0 \le d \le \min(K, i)
$$
and moves exactly $d$ in the allowed direction for that tick.

Notes/clarifications:

- The robot’s position is considered only **after completing** whole ticks. The answer is the smallest integer $n$ such that after finishing tick $n$, the robot is exactly at $(X, Y)$.
- During a tick, the robot cannot “stop early” after moving fewer than $d$ units; it must move exactly the chosen $d$.
- Choosing $d = 0$ is allowed (the robot may stay in place for that tick).
- It is guaranteed that reaching any target with $X \ge 0$ and $Y \ge 0$ is always possible for the given constraints, so the answer always exists (you never need to output $-1$).


For each test case, determine the minimum number of ticks needed to reach exactly $(X, Y)$. If $(X, Y) = (0, 0)$, the answer is $0$.

**Input Format:-**

The first line contains an integer $t$ — the number of test cases.  
Each of the next $t$ lines contains three integers $X$, $Y$, and $K$.

**Output Format:-**

For each test case, output a single integer — the minimum number of ticks required to reach exactly $(X, Y)$.

**Constraints:-**

- $1 \le t \le 10^4$
- $0 \le X, Y \le 10^{18}$
- $1 \le K \le 10^9$

**Examples:-**
 - **Input:**
```
3
2 2 1
2 2 2
2 2 3
```

 - **Output:**
```
4
3
3
```

 - **Input:**
```
5
0 0 7
2 0 1
0 2 1
3 3 2
6 1 3
```

 - **Output:**
```
0
3
4
4
5
```

**Note:-**  
For **Sample Input 1, case 1**, $(X, Y, K) = (2, 2, 1)$. Each tick allows at most $1$ step because $\min(K, i) = 1$ for all $i \ge 1$. So every odd tick can add at most $1$ to $X$, and every even tick can add at most $1$ to $Y$. To reach $X=2$ needs two odd ticks ($i=1,3$) and to reach $Y=2$ needs two even ticks ($i=2,4$), hence the minimum is $4$ ticks.

For **Sample Input 1, case 2**, $(X, Y, K) = (2, 2, 2)$. In $3$ ticks, the maximum possible is:
- on odd ticks $i=1,3$: $X \le \min(2,1)+\min(2,3)=1+2=3$,
- on even tick $i=2$: $Y \le \min(2,2)=2$.
So reaching $(2,2)$ is possible in $3$ ticks, e.g., move $1$ east on tick $1$, $2$ north on tick $2$, and $1$ east on tick $3$.

For **Sample Input 1, case 3**, $(X, Y, K) = (2, 2, 3)$. In $3$ ticks:
- odd ticks $i=1,3$ allow up to $1+3=4$ total east,
- even tick $i=2$ allows up to $2$ total north,
so $(2,2)$ is reachable in $3$ ticks, e.g., move $2$ east on tick $1$, $2$ north on tick $2$, and $0$ on tick $3$.

For **Sample Input 2, case 1**, $(X, Y, K) = (0, 0, 7)$. The robot starts at $(0,0)$, so the minimum number of ticks is $0$.

For **Sample Input 2, case 2**, $(X, Y, K) = (2, 0, 1)$. With $K=1$, each odd tick contributes at most $1$ to $X$. Reaching $X=2$ needs two odd ticks ($i=1$ and $i=3$), and the even tick $i=2$ can be skipped by choosing $d=0$, so the minimum is $3$ ticks.

For **Sample Input 2, case 3**, $(X, Y, K) = (0, 2, 1)$. With $K=1$, each even tick contributes at most $1$ to $Y$. To reach $Y=2$ needs two even ticks ($i=2$ and $i=4$); the odd ticks can use $d=0$, so the minimum is $4$ ticks.

For **Sample Input 2, case 4**, $(X, Y, K) = (3, 3, 2)$. In $4$ ticks:
- odd ticks $i=1,3$: $X \le \min(2,1)+\min(2,3)=1+2=3$,
- even ticks $i=2,4$: $Y \le \min(2,2)+\min(2,4)=2+2=4$.
So $(3,3)$ is reachable in $4$ ticks (for instance, take east moves $1$ and $2$, and north moves $1$ and $2$).

For **Sample Input 2, case 5**, $(X, Y, K) = (6, 1, 3)$. In $5$ ticks:
- odd ticks $i=1,3,5$: $X \le \min(3,1)+\min(3,3)+\min(3,5)=1+3+3=7$,
- even ticks $i=2,4$: $Y \le \min(3,2)+\min(3,4)=2+3=5$.
Thus $(6,1)$ is reachable in $5$ ticks, e.g., move $1$ east on tick $1$, $1$ north on tick $2$, $3$ east on tick $3$, $0$ north on tick $4$, and $2$ east on tick $5$.