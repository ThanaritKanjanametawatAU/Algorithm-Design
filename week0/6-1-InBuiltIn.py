import time
k = int(input())
data = list(map(int,input().split()))
data = sorted(data)

def InMultK(k, data):
    for n in data:
        if k%n==0 and k/n in data:
            print(f"{n} * {k//n} = {k}")
            break

    else:
        print("No Pair Found")

st = time.process_time()
InMultK(k, data)
et = time.process_time()
print(f"Running Time: {et-st}")