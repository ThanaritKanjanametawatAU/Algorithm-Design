import time
import sys
sys.setrecursionlimit(10000)
data = list(map(int, input().split()))
N = len(data)
x = [None for _ in range(N)]
min = sys.maxsize
def BalanceSplit(i):
    global x, N
    if i == N:
        for j in range(N):
            if x[j]:
                pass
        return 1
    else:
        x[i] = 0
        BalanceSplit(i + 1)
        x[i] = 1
        BalanceSplit(i + 1)

st = time.process_time()
print(BalanceSplit(0))
et = time.process_time()
print(f"Running Time: {et-st}")