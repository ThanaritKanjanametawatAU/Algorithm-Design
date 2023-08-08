import sys

data = list(map(int, input().split()))
N = len(data)

x = [None for _ in range(N)]
min_diff = sys.maxsize

def Combination(i):
    global min_diff, x, N
    if i == N:
        group1_sum = sum(data[j] for j in range(N) if x[j] == 0)
        group2_sum = sum(data[j] for j in range(N) if x[j] == 1)
        diff = abs(group1_sum - group2_sum)
        if diff < min_diff:
            min_diff = diff
    else:
        x[i] = 0
        v = Combination(i+1)
        x[i] = 1
        v += Combination(i+1)
        return v

Combination(0)

print(min_diff)