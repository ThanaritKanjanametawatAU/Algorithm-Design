import time
import sys
sys.setrecursionlimit(10000)
N = int(input())

count = 0
def Combination(N):
    global count
    if N <= 0:
        return []
    elif N ==1: # Base Case
        count += 2
        return [[0], [1]]
    else:
        return list(map(lambda x: [0] + x, Combination(N - 1))) + \
               list(map(lambda x: [1] + x, Combination(N - 1)))

st = time.process_time()
for c in Combination(N):
    print(*c)
print(count)
et = time.process_time()
print(f"Running Time: {et-st}")