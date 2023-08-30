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

    def successor(self):
        succ = []
        for v, w in adj_list[self.u]:
            x = state(v, self.g+w)
            x.parent = self
            succ.append(x)
        return succ

    def is_goal(self):
        return self.u == V-1


def UFS(s):
    simplePQ = Simple_Priority_Queue(lambda x,y: x.g < y.g)
    simplePQ.enqueue(s)
    Explored = set()

    while not simplePQ.empty():
        node = simplePQ.dequeue()
        Explored.add(node)
        if node.is_goal():
            return node.g, node

        for suc in node.successor():
            if suc not in Explored:
                simplePQ.enqueue(suc)

def getPath(s):
    # s is goal returned from UFS
    path = []
    while s != None:
        path.insert(0, s.u)
        s = s.parent
    return path

s = state(0, 0)
cost, goal = UFS(s)
path = getPath(goal)

print(cost)
for i in range(len(path)-1):
    print(path[i], end='->')
print(path[-1])