import sys

sys.setrecursionlimit(10000)

# Sample input
n = int(input())
data = list(map(int, input().split()))

# Memoization: Record
memo = [None for _ in range(n + 1)]
def ShoesShopping(d):
    #Memoization: Recall
    if memo[d] is not None:
        return memo[d]

    # Terminating condition
    if d == len(data):
        return 0

    # Recursion: 3 Possible States: Take 1, 2, 3 Shoes
    mincost = sys.maxsize

    # Try taking 1 shoe
    if d <= len(data) - 1:
        Group1 = data[d] + ShoesShopping(d + 1)
        if Group1 < mincost:
            mincost = Group1

    # Try Group by 2 if possible
    if d <= len(data) - 2:
        buffer = data[d:d + 2]
        Group2 = sum(buffer) - (0.5 * min(buffer)) + ShoesShopping(d + 2)
        if Group2 < mincost:
            mincost = Group2

    # Try Group by 3 if possible
    if d <= len(data) - 3:
        buffer = data[d:d + 3]
        Group3 = sum(buffer) - min(buffer) + ShoesShopping(d + 3)
        if Group3 < mincost:
            mincost = Group3

    # Memoization: Record
    memo[d] = mincost
    return mincost

# Dynamic Programming
for i in range(n, -1, -1):
    ShoesShopping(i)
output = memo[0]

# Print Output
print("{:.1f}".format(output))