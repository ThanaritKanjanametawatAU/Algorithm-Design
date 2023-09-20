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

def dfs(i, sumW, sumV):
    global maxV, item, N, M, count

    count += 1
    if i == N:
        # This part consider even if it exceeds capacity
        maxV = max(maxV, sumV) # update maxV
    else:

        dfs(i+1, sumW, sumV) # not take item[i]
        if sumW + item[i].w <= M:
            dfs(i+1, sumW+item[i].w, sumV+item[i].v) # take item[i]

dfs(0,0,0)
print(maxV)
print(count)




    
