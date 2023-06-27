#N = int(input())
import sys

data = list(map(int,input().split()))
N = len(data)
x = [None] * N
minDiff = sys.maxsize
option = [0, 1]
def Comb(i):
    global x, minDiff
    if i == N:
        Sum0 = 0
        Sum1 = 0
        for a in range(N):
            if x[a]:
                Sum1 += data[a]
            else:
                Sum0 += data[a]
        minDiff = min(minDiff, abs(Sum1-Sum0))
    else:
        for o in option:
            x[i] = o
            Comb(i+1)

print(minDiff)