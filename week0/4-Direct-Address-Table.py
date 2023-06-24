import time
k = int(input())
data = list(map(int,input().split()))
DAT = [False for i in range(-12999709,12999709+1)]
def DATMultK(k,data):
    for n in data:
        if k%n==0 and DAT[k//n]:
            print(f"{n} * {k//n} = {k}")
            break
        else:
            DAT[n] = True

    else:
        print("No Pair Found")

st = time.process_time()
DATMultK(k,data)
et = time.process_time()
print(f"Running Time: {et-st}")
