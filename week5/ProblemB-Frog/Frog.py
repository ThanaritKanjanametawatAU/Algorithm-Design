N = int(input())
H = list(map(int, input().split()))
frogs = [0] * N

def Frog(i):
    global N, H, frogs

    if i == 0:
        return 0

    if frogs[i] != 0:
        return frogs[i]

    cost = Frog(i - 1) + abs(H[i] - H[i - 1])

    if i > 1:
        cost = min(cost, Frog(i - 2) + abs(H[i] - H[i - 2]))

    frogs[i] = cost
    return cost


print(Frog(N - 1))
