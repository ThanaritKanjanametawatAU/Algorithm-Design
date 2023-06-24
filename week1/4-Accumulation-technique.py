import sys
import time
data = list(map(int,input().split()))

def Sum(accList,left,right):
    if left == 0:
        return accList[right]

    return accList[right] - accList[left-1]


def AccumulationTechnique(data):
    accList = []
    acc = 0
    for d in data:
        acc += d
        accList.append(acc)

    max = (-1) * sys.maxsize
    for i in range(len(accList)):
        for j in range(i,len(accList)):
            SumIJ = Sum(accList, i, j)
            if SumIJ > max:
                max = SumIJ

    return max



st = time.process_time()
print(AccumulationTechnique(data))
et = time.process_time()
print(f"Running Time: {et-st}")