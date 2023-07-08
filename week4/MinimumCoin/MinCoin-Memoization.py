import sys
import time
sys.setrecursionlimit(10000)
CoinChoice = list(map(int,input().split()))
v = int(input())
MinCoin = [None for _ in range(v+1)]
MinCoin[0] = 0
calls = [0 for _ in range(v+1)]
def mincoin(v):
    if MinCoin[v] != None:
        return MinCoin[v]

    calls[v] += 1
    minX = sys.maxsize
    for c in CoinChoice:
        if c <= v:
            minX = min(minX, 1 + mincoin(v-c))

    MinCoin[v] = minX

    return MinCoin[v]

st = time.process_time()
print(mincoin(v))
print(calls)
et = time.process_time()
print(f"Running Time: {et-st}")