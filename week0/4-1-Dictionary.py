import time
k = int(input())
data = list(map(int,input().split()))
def DictMultK(k,data):
    Dict = {}
    for n in data:
        try:
            compliment = k/n
            Dict[compliment]

        except KeyError:
            Dict[n] = True

        else:
            print(f"{n} * {int(compliment)} = {k}")
            break

    else:
        print("No Pair Found")


st = time.process_time()
DictMultK(k, data)
et = time.process_time()
print(f"Running Time: {et-st}")
