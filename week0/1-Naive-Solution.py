import time
k = int(input())
data = list(map(int,input().split()))

def NaiveMultK(k, data):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i]*data[j]==k:
                print(f"{data[i]} * {data[j]} = {k}")
                break
        else:
            continue
        break

    else:
        print("No Pair Found")

st = time.process_time()
NaiveMultK(k, data)
et = time.process_time()
print(f"Running Time: {et-st}")