N, C = map(int, input().split())
w = []
v = []
for _ in range(N):
    vi, wi = map(int, input().split())
    w.append(wi)
    v.append(vi)

MaximumValue = [[None for _ in range(C+1)] for _ in range(N+1)]
MaximumValue[N] = [0 for _ in range(C+1)]

def KnapsackDynamicProgramming():
    for i in range(N-1,-1,-1):
        for j in range(C+1):
            notChoose = MaximumValue[i+1][j]
            if w[i] <= j:
                Choose = v[i] + MaximumValue[i+1][j-w[i]]
            else:
                Choose = -1

            MaximumValue[i][j] = max(Choose, notChoose)

    return MaximumValue[0][C]
print(KnapsackDynamicProgramming())