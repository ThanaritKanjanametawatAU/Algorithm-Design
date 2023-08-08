import time
import sys
sys.setrecursionlimit(10000)
N = int(input())
k = int(input())
x = [None for _ in range(N)]

def Combination(i, s):
    global x, N, k
    if s == k:
        for j in range(N):
            if x[j] == None:
                x[j] = 0
        print(*x)
        return 1
    elif N-i == k-s:   # Change this line
        for j in range(i, N):   # And also change to start from i
            x[j] = 1
        print(*x)
        for j in range(i, N):   # reset values for next recursion
            x[j] = None
        return 1
    elif N-i+s < k:
        return 0
    else:
        x[i] = 0
        v = Combination(i+1, s)
        x[i] = 1
        v += Combination(i+1, s+1)
        x[i] = None   # Add this line to reset value for next recursion
        return v

st = time.process_time()
print(Combination(0, 0))
et = time.process_time()
print(f"Running Time: {et-st}")
