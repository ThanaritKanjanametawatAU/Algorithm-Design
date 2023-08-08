import time
import sys
sys.setrecursionlimit(10000)
N = int(input())
x = [None for _ in range(N)]
option = ["A", "B", "C"]
def Combination(i):
    global x, N, option
    if i == N:
        print(*x)
        return 1
    else:
        v = 0
        for o in option:
            x[i] = o
            v += Combination(i+1)
        return v

st = time.process_time()
print(Combination(0))
et = time.process_time()
print(f"Running Time: {et-st}")