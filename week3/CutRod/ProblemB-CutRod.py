import sys
import time
sys.setrecursionlimit(10000)
Price = list(map(int, input().split()))
l = len(Price)
count = 0
def RodCut(l):
    global count
    count += 1
    if l == 0:
        return 0

    maxRev = 0
    for i in range(1, l + 1):
        maxRev = max(maxRev, Price[i-1] + RodCut(l - i))
    return maxRev


st = time.process_time()
print(RodCut(l))
print(count)
et = time.process_time()
print(f"Running Time: {et - st}")
