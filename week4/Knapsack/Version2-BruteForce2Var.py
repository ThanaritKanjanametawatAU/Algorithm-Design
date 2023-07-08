import time
N, C = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
calls = [0 for _ in range(N+1)]
def maxVal(i, C):
    calls[i] += 1
    if i==N:
        return 0

    notChoose = maxVal(i + 1, C)
    if w[i] <= C:
        Choose = v[i] + maxVal(i+1,C-w[i])
    else:
        Choose = -1
    return max(Choose, notChoose)


st = time.process_time()
print(maxVal(0, C))
print(calls)
et = time.process_time()
print(f"Running Time: {et-st}")