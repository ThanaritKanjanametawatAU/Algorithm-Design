import time
import sys

data = list(map(int,input().split()))
def Sum(data,left,right):
    s = 0
    for k in range(left,right+1):
        s += data[k]
    return s

def StraightForwardSolution(data):
    max = (-1) * sys.maxsize
    for i in range(len(data)):
        for j in range(i, len(data)):
            SumIJ = Sum(data, i, j)
            if SumIJ > max:
                max = SumIJ

    print(max)

st = time.process_time()
StraightForwardSolution(data)
et = time.process_time()
print(f"Running Time: {et-st}")