import sys
data = list(map(int,input().split()))
count = 0
def Combination(N):
    global count
    if N <= 0:
        return []
    elif N ==1:
        count += 2
        return [[0], [1]]
    else:
        return list(map(lambda x: [0] + x, Combination(N - 1))) + \
               list(map(lambda x: [1] + x, Combination(N - 1)))

def BruteForce(data):
    minDiff = sys.maxsize
    for c in Combination(len(data)):
        Sum0 = 0
        Sum1 = 0
        for i in range(len(c)):
            if c[i]:
                Sum1 += data[i]
            else:
                Sum0 += data[i]

        minDiff = min(minDiff, abs(Sum1-Sum0))

    return minDiff

print(BruteForce(data))
