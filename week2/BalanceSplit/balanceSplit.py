import sys
sys.setrecursionlimit(10000)

nList = list(map(int, input().split()))
n = len(nList)
x = [None] * n
sumList = []
min_value = 999999

def comb(i):
    global x
    if i == n:
        print(x)
        sumList.append(sum(x))
    else:
        x[i] = 0
        comb(i+1)
        x[i] = nList[i]
        comb(i+1)
        
comb(0)

for i in range(len(sumList)//2):
    if i == 0:
        result = abs(sumList[0] - sumList[-1])
    else:
        result = abs(sumList[i] - sumList[-i-1])
        
    if result > 0 and result < min_value:
        min_value = result
        
print(min_value)
