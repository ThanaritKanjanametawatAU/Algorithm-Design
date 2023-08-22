import time
rows, cols = map(int, input().split())
Srow, Scol = map(int, input().split())
Drow, Dcol = map(int, input().split())
maze = []
adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# 0 is path, 1 is wall
for i in range(rows):
    maze.append(list(input().split()))

class state():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.g = 0 # number of steps from start to this state
        self.parent = None

def valid(i, j):
    return 0 <= i < rows and 0 <= j < cols and maze[i][j] == '0'

def successor(s):
    succ = []
    for y,x in adj:
        if valid(s.i+y, s.j+x):
            x = state(s.i+y, s.j+x)
            x.g = s.g + 1
            x.parent = s
            succ.append(x)
    return succ
def is_goal(s):
    return s.i == Drow and s.j == Dcol

def stateEqual(s1, s2):
    return s1.i == s2.i and s1.j == s2.j

def BFS(s):
    Q = [s]
    Reached = set()
    Reached.add((s.i, s.j))
    while Q:
        node = Q[0]
        del Q[0]
        if is_goal(node):
            return node.g
        for suc in successor(node):
            if (suc.i, suc.j) not in Reached:
                Reached.add((suc.i,suc.j))
                Q.append(suc)
s = state(Srow, Scol)
print(s.i, s.j)
print(BFS(s))