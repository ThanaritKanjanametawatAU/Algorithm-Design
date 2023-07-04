import time
N = int(input())
Colors = []
for _ in range(N):
    Colors.append(tuple(map(int, input().split())))

def UltimateGreyness(N, Colors):

    return
st = time.process_time()
print(UltimateGreyness(N, Colors))
et = time.process_time()
print(f"Running Time: {et-st}")