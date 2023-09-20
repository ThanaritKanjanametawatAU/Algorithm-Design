n = int(input())
x = list(map(int, input().split()))
y = []
i = 0
while i < len(x):
    y.append((x[i], x[i + 1]))
    i += 2

# y = [(2, 1), (7, 6), (9, 3), (18, 4), (3, 2), (5, 5)]

def ComparePairs(p1, p2): # p1 > p2
    return p1[0] > p2[0] and p1[1] < p2[1]

def merge(A, left, middle, right):
    global Total
    B = []
    i = left
    j = middle + 1
    while i <= middle and j <= right:
        if ComparePairs(A[i], A[j]):
            B.append(A[i])
            i += 1
        else:
            print(A[i:middle + 1], A[j:right + 1])
            Total += len(A[i:middle + 1])
            B.append(A[j])
            j += 1
    A[left:right + 1] = B + A[i:middle + 1] + A[j:right + 1]


def mergesort(A, left, right):
    if left < right:
        middle = (left + right) // 2
        mergesort(A, left, middle)
        mergesort(A, middle + 1, right)
        merge(A, left, middle, right)


# y.sort(key=lambda p: (-p[0], p[1]))
Total = 0
mergesort(y, 0, len(y) - 1)
print(Total)
print("{")