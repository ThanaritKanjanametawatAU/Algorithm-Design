import time
N = int(input())
Q = [None for _ in range(N)]
def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

def conflict(Q, i, j):
    #Check Horizontal and Diagonal
    return Q[i] == Q[j] or abs(Q[i]-Q[j]) == abs(i-j)

class state():
    def __init__(self, Q):
        self.Q = Q
        self.g = 0  # Current Modifying Column Index
        self.parent = None


def stateEqual(s1, s2):
    return s1.Q == s2.Q


def successor(s):
    if s.g == N:  # If Board is Full, There is no successor
        return []

    succ = []
    for j in range(N):
        newQ = s.Q.copy()
        newQ[s.g] = j

        x = state(newQ)

        no_conflict = True
        for k in range(s.g):
            if conflict(x.Q, k, s.g):
                no_conflict = False
                break

        if no_conflict:
            x.g = s.g + 1
            x.parent = s
            succ.append(x)

    return succ


def is_goal(s):
    return sum([1 for i in range(N) if s.Q[i]==None]) == 0

def BreadthFirstSearch(s):
    Q = [s]
    Reached = set()
    Reached.add(tuple(s.Q))
    while Q:
        node = Q[0]
        del Q[0]
        if is_goal(node):
            return node.g
        for suc in successor(node):
            if tuple(suc.Q) not in Reached:
                Reached.add(tuple(suc.Q))
                Q.append(suc)
def BreadthFirstSearch(s):
    global count
    Q = [s]
    Reached = set()
    Reached.add(s)
    solution = []
    while Q:
        node = Q[0]
        del Q[0]

        if is_goal(node):
            exist = False
            for s1 in solution:
                if stateEqual(s1, node):
                    exist = True
                    break
            if not exist:
                print(f"Solution #{len(solution)+1}")
                printqueens(node.Q)
                solution.append(node)

        for suc in successor(node):
            SInReached = False
            for d in Reached:
                if stateEqual(d, suc):
                    SInReached = True
                    break

            if not SInReached:
                Reached.add(suc)
                Q.append(suc)


s = state(Q)
BreadthFirstSearch(s)