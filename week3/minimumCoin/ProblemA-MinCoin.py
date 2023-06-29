import sys
import time
sys.setrecursionlimit(10000)
CoinChoice = list(map(int,input().split()))
k = int(input())
count = 0
def mincoin(v):
    global count
    count += 1
    if v <= 0:
        return 0

    minX = sys.maxsize
    for c in CoinChoice:
        if c <= v:
            minX = min(minX, 1 + mincoin(v-c))

    return minX

st = time.process_time()
print(mincoin(k))
print(count)
et = time.process_time()
print(f"Running Time: {et-st}")