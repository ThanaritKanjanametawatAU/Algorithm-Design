import sys
#N = int(input())
N = 3
def f(i, s):
    if i == N:
        return 1
    else:
        return f(i+1, s+1)
print()
data = list(map(int,input().split()))
N = len(data)
x = [None] * N
combination = []
option = [0, 1]
def Comb(i, s):
    global x, combination
    if i == N:
        Sum0 = 0
        Sum1 = 0
        for a in range(N):
            if x[a]:
                Sum1 += data[a]
            else:
                Sum0 += data[a]
        combination.append(abs(Sum1-Sum0))
    else:
        for o in option:
            x[i] = o
            Comb(i+1)

def BruteForce(data):
    Comb(0)
    return min(combination)

print(BruteForce(data))