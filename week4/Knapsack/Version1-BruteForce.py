import time
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
x = [0] * N
def comb(i):
    if i == N:
        sw = sv = 0
        for j in range(N):
            if x[j]:
                sw += w[j]
                sv += v[j]
        if sw > M:
            return -1
        else:
            return sv
    else:
        x[i] = 0  # Not Choose
        a = comb(i+1)
        x[i] = 1 # Choose
        b = comb(i+1)
        return max(a,b)

st = time.process_time()
print(comb(0))
et = time.process_time()
print(f"Running Time: {et-st}")