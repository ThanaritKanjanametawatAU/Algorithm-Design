class obj:
    def __init__(self,w,v):
        self.w = w
        self.v = v
        self.r = v/w

x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
item = []
for i in range(N):
    item.append(obj(int(w[i]),int(v[i])))

maxV = 0
count = 0

def Bound(i, sumW, sumV):
    global item, N, M

    RightWeight = 0
    SV = 0
    propotion = 1
    j = i + 1

    # proportion == 1 means the item[j] can be put into the knapsack physically
    # M-sumW-RightWeight > 0 means there is still space in the knapsack

    # j < N means there are still items to be considered
    while j < N and propotion == 1:
        # if the item[j] can be put into the knapsack physically then propotion is 1
        # otherwise propotion is the proportion of the item[j] that can be put into the knapsack

        propotion = min(M - sumW - RightWeight, item[j].w) / item[j].w
        RightWeight += propotion * item[j].w
        SV += propotion * item[j].v
        j += 1

    return SV + sumV

def dfs(i, sumW, sumV):
    global maxV, item, N, M, count

    count += 1
    if i == N:
        maxV = max(maxV, sumV) # update maxV
    else:
        if sumW + item[i].w <= M: # only consider if it is possible to put item[i] into the knapsack
            dfs(i+1, sumW+item[i].w, sumV+item[i].v)

        if Bound(i, sumW, sumV) > maxV: # only consider if it is possible to get a better solution
            dfs(i+1, sumW, sumV)

item.sort(key=lambda x: x.r, reverse=True)
dfs(0,0,0)
print(maxV)
print(count)