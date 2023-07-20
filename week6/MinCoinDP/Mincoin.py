import sys
import time
sys.setrecursionlimit(10000)
CoinChoice = list(map(int,input().split()))
k = int(input())
count = 0
MinCoin = [None for _ in range(k+1)]
MinCoin[0] = 0
Solution = [[] for _ in range(k+1)]
def mincoinDynamicProgramming(v):
    for i in range(1,v+1):
        MinCoin[i] = sys.maxsize
        for c in CoinChoice:
            if c <= i:
                if MinCoin[i] >= 1 + MinCoin[i-c]:
                    MinCoin[i] = 1 + MinCoin[i-c]

                    Solution[i] = Solution[i-c] + [c]

    return MinCoin[v], Solution[v]

st = time.process_time()
print(k)
print(mincoinDynamicProgramming(k))
et = time.process_time()
print(f"Running Time: {et-st}")