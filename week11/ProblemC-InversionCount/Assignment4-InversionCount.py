def conquer(A, left, middle, right):
    global Total
    B = []
    i = left
    j = middle + 1
    while i <= middle and j <= right:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            Total += (middle - i + 1)
            B.append(A[j])
            j += 1
    A[left:right + 1] = B + A[i:middle + 1] + A[j:right + 1]

def divide(A, left, right):
    if left < right:
        middle = (left + right) // 2
        divide(A, left, middle)
        divide(A, middle + 1, right)
        conquer(A, left, middle, right)

t = int(input())  # Number of testcases
for _ in range(t):
    _ = input()  # Blank line
    n = int(input())  # Size of array
    A = [int(input()) for _ in range(n)]
    Total = 0
    divide(A, 0, len(A) - 1)
    print(Total)
