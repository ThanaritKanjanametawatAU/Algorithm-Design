N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

def KadaneAlgorithm(data):
   maxGlobal = 0
   maxLocal = 0
   for d in data:
       maxLocal += d
       maxLocal = max(maxLocal, 0)
       maxGlobal = max(maxLocal, maxGlobal)

   return maxGlobal

print(KadaneAlgorithm(data))