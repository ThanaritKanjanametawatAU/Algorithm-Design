import time
import sys
sys.setrecursionlimit(10000)
N = int(input())
Colors = []
for _ in range(N):
    Colors.append(tuple(map(int, input().split())))

x = [None for _ in range(N)]
minDiff = sys.maxsize
minRes = None
def Combination(i):
    global x, N, minDiff, minRes
    if N <= 0:
        return
    if i == N:
        if sum(x) != 0:
            vividness, dullness = 1, 0
            for j in range(N):
                if x[j]:
                    vividness *= Colors[j][0]
                    dullness += Colors[j][1]
            if (y:=abs(vividness-dullness)) < minDiff:
                minDiff = y
                minRes = x.copy()

    else:
        x[i] = 0
        Combination(i+1)
        x[i] = 1
        Combination(i+1)


st = time.process_time()
Combination(0)
print(minDiff)
print(minRes)
et = time.process_time()
print(f"Running Time: {et-st}")