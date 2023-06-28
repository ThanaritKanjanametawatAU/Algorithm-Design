import time
import sys
sys.setrecursionlimit(10000)
N = int(input())
k = int(input())
x = [None for _ in range(N)]


def Combination(i):
    global x, N, k
    if i == N:
        if sum(x) == k:
            print(*x)
            return 1
        return 0
    else:
        x[i] = 0
        v = Combination(i+1)
        x[i] = 1
        v += Combination(i+1)
        return v

st = time.process_time()
print(Combination(0))
et = time.process_time()
print(f"Running Time: {et-st}")