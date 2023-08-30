import time
from week9.FireProblem.module.notSimplePriorityQueue import *

V = int(input())
adj_list = [[] for _ in range(V)]
while True:
    try:
        u, v, w = map(int, input().split())
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    except:
        break



class state:
    def __init__(self, u, g):
        self.u = u
        self.g = g
        self.parent = None
        self.index = None

    def precede(self, x):
        return self.g < x.g

    def assign(self, v):
        x = state(self.u, v)
        if not self.precede(x):
            self.g = v
            return True
        else:
            return False

def successor(s):
    succ = []
    for v, w in adj_list[s.u]:
        x = state(v, s.g+w)
        x.parent = s
        succ.append(x)
    return succ

def stateEqual(s1, s2):
    return s1.u == s2.u
def is_goal(s):
    return s.u == V-1

def UFS(s):
    # Use pq.elevate_key
    pq = Priority_Queue()
    s.index = 0
    pq.enqueue(s)

    Reached = set()
    Reached.add(s)

    while not pq.empty():
        node = pq.dequeue()

        if is_goal(node):
            return node.g, node

        for suc in successor(node):
            SInReached = False
            for d in Reached:
                if stateEqual(d, suc):
                    SInReached = True
                    break

            if not SInReached:
                Reached.add(suc)
                suc.index = len(pq.a)
                pq.enqueue(suc)

            else:
                for d in pq.a:
                    if stateEqual(d, suc):
                        if suc.g < d.g:
                            d.g = suc.g
                            pq.elevate_key(d, suc.g)
                        break
def getPathList(goalnode):
    path = []
    while goalnode != None:
        path.append(goalnode.u)
        goalnode = goalnode.parent
    path.reverse()
    return path

st = time.process_time()

mincost, goalnode = UFS(state(0, 0))
print(mincost)

path = getPathList(goalnode)
for i in range(len(path)-1):
    print(f"{path[i]} -> ", end='')
print(path[-1])

et = time.process_time()
print(f"Running Time: {et-st}")