# Input
N, M = map(int, input().split())
Ns = list(map(int, input().split()))
Ms = list(map(int, input().split()))

# Memoization: Record
LCS = [[None for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    LCS[i][M] = 0
for j in range(M + 1):
    LCS[N][j] = 0


def LCSLength(i, j):
    # Memoization: Recall
    if LCS[i][j] != None:
        return LCS[i][j]

    # Terminating
    if i == N or j == M:
        return 0

    # Recursion
    LongestLength = 0
    if Ns[i] == Ms[j]:
        LongestLength = 1 + LCSLength(i + 1, j + 1)
    else:
        LongestLength = max(LCSLength(i + 1, j), LCSLength(i, j + 1))


    # Memoization: Record
    LCS[i][j] = LongestLength
    return LCS[i][j]

# Dynamic Programming
for i in range(N, -1, -1):
    for j in range(M, -1, -1):
        LCSLength(i, j)
result = LCS[0][0]

# Output
print(result)
