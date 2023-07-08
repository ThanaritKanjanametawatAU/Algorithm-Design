import sys
import time

sys.setrecursionlimit(10000)
Price = list(map(int, input().split()))
l = len(Price)
count = 0
calls = [0 for _ in range(l+1)]
MaximumRevenue = [None for _ in range(l + 1)]
MaximumRevenue[0] = 0
def RodCut(l):
    global MaximumRevenue, calls, count
    if MaximumRevenue[l] == None:
        calls[l] += 1
        count += 1

        maxRev = -1
        for i in range(1, l + 1):
            maxRev = max(maxRev, Price[i-1] + RodCut(l-i))

        MaximumRevenue[l] = maxRev



    return MaximumRevenue[l]



st = time.process_time()
print(RodCut(l))
print(count)
print(calls)
et = time.process_time()
print(f"Running Time: {et - st}")
