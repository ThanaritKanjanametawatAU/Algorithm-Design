import time
import sys
sys.setrecursionlimit(10000)
A = input()
B = input()
ed = [[-1 for i in range(len(B)+1)] for j in range(len(A)+1)]

def EditDistance(i, j):
    global A, B, ed

    if ed[i][j] != -1:
        return ed[i][j]

    if i == len(A):
        return len(B) - j
    elif j == len(B):
        return len(A) - i

    elif A[i] == B[j]:
        answer = EditDistance(i+1, j+1)
    else:
        delete = 1 + EditDistance(i+1, j)
        insert = 1 + EditDistance(i, j+1)
        substitute = 1 + EditDistance(i+1, j+1)
        answer = min(delete, insert, substitute)

    ed[i][j] = answer
    return answer

st = time.process_time()
print(EditDistance(0, 0))
et = time.process_time()
print(f"Running Time: {et-st}")
