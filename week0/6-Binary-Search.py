import time
k = int(input())
data = list(map(int,input().split()))
# data must be sorted for Binary Search
data.sort()

def BinarySearch(target, data, L=0, R=len(data)-1):
    if L > R:
        return False

    else:
        mid = L + (R - L) //2

        try:
            data[mid]
        except IndexError:
            return False


        if data[mid] == target:
            return True

        elif data[mid] > target:
            return BinarySearch(target, data, L, mid-1)

        else:
            return BinarySearch(target, data, mid+1, R)

def BinarySearchMultK(k, data):
    for n in data:
        i = data.index(n)
        del data[i]
        if k%n == 0 and BinarySearch(k//n,data):
            print(f"{n} * {k//n} = {k}")
            break
        data.insert(i,n)

    else:
        print("No Pair Found")

st = time.process_time()
BinarySearchMultK(k,data)
et = time.process_time()
print(f"Running Time: {et-st}")