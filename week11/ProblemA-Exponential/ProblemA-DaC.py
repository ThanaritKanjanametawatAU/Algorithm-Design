a = 13
x = 10**18
mod = 2147483647 # For Displaying Purposes

def expoponential(a, x):
    if x == 0:
        return 1
    else:
        SqrtA = expoponential(a, x // 2)

        if x % 2 == 0:
            return (SqrtA * SqrtA) % mod
        else:
            return ((SqrtA * SqrtA) * a) % mod

print(expoponential(a, x))