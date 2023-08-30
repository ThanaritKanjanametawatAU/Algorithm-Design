import heapq

N = int(input())
House = [list(map(int, input().split())) for _ in range(N)]

PQ = []
heapq.heappush(PQ, House[N-1][N-1])
p = 0
for i in range(2*N-1, 0, -1):
    u = -heapq.heappop(PQ)
    if i != 2*N-1:
        p += u

    for j in range(N):
        if 0 <= i-1-j < N:
            heapq.heappush(PQ, -House[j][i-1-j])

print(p)
