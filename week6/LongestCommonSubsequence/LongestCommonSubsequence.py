import time
N, M = map(int, input().split())
Ns = list(map(int, input().split()))
Ms = list(map(int, input().split()))
LCS = [[None for _ in range(M+1)] for _ in range(N+1)]
LCS[N] = [0 for _ in range(M+1)]
def LCSLength(i, j):
    if LCS[i][j] != None:
        return LCS[i][j]

    if Ns[i] == Ms[j]:
        LCS[i][j] = 1 + LCSLength(i+1, j+1)
    else:
        LCS[i][j] = max(LCSLength(i+1, j), LCSLength(i, j+1))

    return LCS[i][j]
st = time.process_time()
print(LCSLength(0,0))
et = time.process_time()
print(f"Running Time: {et-st}")