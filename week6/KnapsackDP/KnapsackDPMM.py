import time
N, C = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
MaximumValue = [[None for _ in range(C+1)] for _ in range(N+1)]
MaximumValue[N] = [0 for _ in range(C+1)]
count = 0
def maxVal(i, C):
    if MaximumValue[i][C] != None:
        return MaximumValue[i][C]

    notChoose = maxVal(i + 1, C)
    if w[i] <= C:
        Choose = v[i] + maxVal(i+1,C-w[i])
    else:
        Choose = -1

    MaximumValue[i][C] = max(Choose, notChoose)
    return MaximumValue[i][C]

def KnapsackDynamicProgramming():
    for i in range(N-1,-1,-1):
        for j in range(C+1):
            maxVal(i, j)

st = time.process_time()
KnapsackDynamicProgramming()
print(MaximumValue[0][C])
et = time.process_time()
print(f"Running Time: {et-st}")