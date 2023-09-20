# Divide and Conquer for maximum contiguous subarray
x = list(map(int, input().split()))
n = len(x)

def maxCrossingSum(x, left, middle, right):
    sum = 0
    leftSum = -1
    for i in range(middle, left - 1, -1):
        sum += x[i]
        if sum > leftSum:
            leftSum = sum

    sum = 0
    rightSum = -1
    for i in range(middle + 1, right + 1):
        sum += x[i]
        if sum > rightSum:
            rightSum = sum


    return leftSum + rightSum

def maxSubArraySum(x, left, right):
    if left == right:
        return x[left]

    middle = (left + right) // 2

    return max(maxSubArraySum(x, left, middle),
               maxSubArraySum(x, middle + 1, right),
               maxCrossingSum(x, left, middle, right))

print(maxSubArraySum(x, 0, n - 1))