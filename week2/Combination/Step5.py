import time
import sys
sys.setrecursionlimit(10000)
N = int(input())
x = [None] * N
option = ["A","B","C"]
def Comb(i):
    global x
    if i == N:
        return 1
    else:
        s = 0
        for o in option:
            x[i] = o
            s += Comb(i+1)
        return s


st = time.process_time()
print(Comb(0))
et = time.process_time()
print(f"Running Time: {et-st}")