import sys
import time
from week9.FireProblem.module.simplePriorityQueue import *

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
    global count
    pq = Simple_Priority_Queue(lambda x,y: x.g < y.g)
    pq.enqueue(s)
    MinCost = [sys.maxsize for _ in range(V)]

    Reached = set()
    Reached.add(s)
    while not pq.empty():
        node = pq.dequeue()

        if is_goal(node):
            return MinCost[node.u], node

        for suc in successor(node):
            SInReached = False
            for d in Reached:
                if stateEqual(d, suc):
                    SInReached = True
                    break

            if not SInReached:
                Reached.add(suc)
                pq.enqueue(suc)

            if suc.g < MinCost[suc.u]:
                MinCost[suc.u] = suc.g
                pq.enqueue(suc)

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