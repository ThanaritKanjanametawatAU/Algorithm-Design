a = 2
x = 10
mod = 2147483647 # For Displaying Purposes

def exponential(a, x):
    result = 1
    for i in range(x):
        result *= a
    return result % mod

print(exponential(a, x))