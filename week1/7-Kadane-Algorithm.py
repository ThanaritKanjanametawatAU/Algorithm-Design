import sys
import time
data = list(map(int,input().split()))

def KadaneAlgorithm(data):
    maxGlobal = data[0]
    maxLocal = data[0]

    for i in range(1, len(data)):
        maxLocal = max(data[i], maxLocal + data[i])
        maxGlobal = max(maxGlobal, maxLocal)

    return max(maxGlobal,0)

st = time.process_time()
print(KadaneAlgorithm(data))
et = time.process_time()
print(f"Running Time: {et-st}")