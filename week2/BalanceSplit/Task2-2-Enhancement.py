import sys

data = list(map(int, input().split()))
N = len(data)

x = [None for _ in range(N)]
min_diff = sys.maxsize

def Combination(i, group1_sum):
    global min_diff, x, N
    if i == N:
        group2_sum = total_sum - group1_sum
        diff = abs(group1_sum - group2_sum)
        if diff < min_diff:
            min_diff = diff
        return 1
    else:
        x[i] = 0
        v = Combination(i+1, group1_sum + arr[i])
        x[i] = 1
        v += Combination(i+1, group1_sum)
        return v

Combination(0)

print(min_diff)