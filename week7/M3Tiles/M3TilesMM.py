import sys
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

memo = [[None for _ in range(3)] for _ in range(L+1)] # Add

def nWays(d, s):
    if memo[d][s] != None:    # Add
        return memo[d][s]

    if d == L:
        if s == FLAT:
            return 1
        else:
            return 0
    else:
        counter = 0
        if s == FLAT:
            counter += nWays(d+1, UPPER2)
            counter += nWays(d+1, LOWER2)   # Actually, this is symmetric to UPPER2
            if d < L-1: # Check if we can put a tile at d+2
                counter += nWays(d+2, FLAT)
        else:  # s is either UPPER2 or LOWER2
            counter += nWays(d+1,FLAT)
            if d < L-1:
                counter += nWays(d+2, s)

        # Add
        memo[d][s] = counter
        return memo[d][s]
print(nWays(0, FLAT))


