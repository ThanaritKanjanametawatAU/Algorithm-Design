import time
import sys
sys.setrecursionlimit(10000)

N = int(input())
k = int(input())
count = 0

def Combination(N, k):
    global count
    if N < k or N <= 0:
        return []
    elif k == 0:
        count += 1
        return [[0] * N]
    elif N == k:
        count += 1
        return [[1] * k]

    else:
        return list(map(lambda x: [0] + x, Combination(N - 1, k))) + \
               list(map(lambda x: [1] + x, Combination(N - 1, k - 1)))

st = time.process_time()
for c in Combination(N, k):
    print(*c)
print(count)
et = time.process_time()
print(f"Running Time: {et-st}")
