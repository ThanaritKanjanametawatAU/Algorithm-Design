import time
import sys
sys.setrecursionlimit(10000)
N = int(input())
k = int(input())
x = [None] * N
def Comb(i):
    global x
    if i == N:
        if x.count(1) == k:
            return 1
        else:
            return 0
    else:
        x[i] = 0
        s = Comb(i+1)
        x[i] = 1
        s += Comb(i+1)
        return s


st = time.process_time()
print(Comb(0))
et = time.process_time()
print(f"Running Time: {et-st}")