import sys
import time
N = int(input())
data = list(map(int,input().split()))

def Combination(N, data):
    if N <= 0:
        return [([], 0)]
    else:
        return [([0] + x, s) for x, s in Combination(N - 1, data[:-1])] + \
               [([1] + x, s + data[-1]) for x, s in Combination(N - 1, data[:-1])]

def Enhancement(data):
    minDiff = sys.maxsize
    for c, sum1 in Combination(len(data), data):
        sum0 = sum(data) - sum1
        minDiff = min(minDiff, abs(sum1-sum0))

    return minDiff

print(Enhancement(data))