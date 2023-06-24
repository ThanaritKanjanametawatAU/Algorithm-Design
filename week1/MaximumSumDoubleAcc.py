N = int(input())
Matrix = []
for _ in range(N):
    Matrix.append(list(map(int, input().split())))


def Sum(accMatrix, a, b, c, d):
    if a == 0 and c == 0:
        return accMatrix[b][d]
    if a == 0:
        return accMatrix[b][d] - accMatrix[b][c - 1]
    if c == 0:
        return accMatrix[b][d] - accMatrix[a - 1][d]

    return accMatrix[b][d] - accMatrix[b][c - 1] - accMatrix[a - 1][d] + accMatrix[a - 1][
        c - 1]  # ,  accMatrix[b][d], accMatrix[b][c-1], accMatrix[a-1][d], accMatrix[a-1][c-1]


def SubMatrixSum(Matrix, r, c):
    sum = 0
    for a in range(r + 1):
        for b in range(c + 1):
            sum += Matrix[a][b]
    return sum


def MaximumSumDoubleAcc(Matrix):
    accMatrix = [[0 for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            accMatrix[a][b] = SubMatrixSum(Matrix, a, b)

    max = 0
    for a in range(N):
        for b in range(a, N):
            for c in range(N):
                for d in range(c, N):
                    sumABCD = Sum(accMatrix, a, b, c, d)
                    if sumABCD > max:
                        max = sumABCD
    return max


print(MaximumSumDoubleAcc(Matrix))
