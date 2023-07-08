import sys
import time
sys.setrecursionlimit(10000)
Price = list(map(int, input().split()))
l = len(Price)
count = 0
calls = [0 for _ in range(l+1)]
def RodCut(l):
    global count, calls
    calls[l] += 1
    count += 1
    if l == 0:
        return 0

    maxRev = -1
    for i in range(1, l + 1):
        maxRev = max(maxRev, Price[i-1] + RodCut(l - i))

    return maxRev


st = time.process_time()
print(RodCut(l))
print(count)
print(calls)
et = time.process_time()
print(f"Running Time: {et - st}")
