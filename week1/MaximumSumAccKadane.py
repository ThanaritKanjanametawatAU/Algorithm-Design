import sys

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

def KadaneAlgorithm(data):
    maxGlobal = data[0]
    maxLocal = data[0]

    for i in range(1, len(data)):
        maxLocal = max(data[i], maxLocal + data[i])
        maxGlobal = max(maxGlobal, maxLocal)

    return maxGlobal

def maxSubmatrixSum(N, M):
    max_sum = (-1) * sys.maxsize

    for left in range(N):
        temp = [0] * N

        for right in range(left, N):
            for i in range(N):
                temp[i] += M[i][right]

            max_sum = max(max_sum, KadaneAlgorithm(temp))


    return max_sum



print(maxSubmatrixSum(N, M))
