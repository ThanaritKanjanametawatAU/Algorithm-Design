import time
import sys
sys.setrecursionlimit(10000)
N = int(input())

count = 0
def Combination(N):
    global count
    options = ["A", "B", "C"]
    if N <= 0:
        return []
    elif N ==1:
        count += len(options)
        return list(map(lambda x: [x], options))
    else:
        result = []
        for o in options:
            result += list(map(lambda x: [o] + x, Combination(N - 1)))

        return result
st = time.process_time()
for c in Combination(N):
    print(*c)
print(count)
et = time.process_time()
print(f"Running Time: {et-st}")