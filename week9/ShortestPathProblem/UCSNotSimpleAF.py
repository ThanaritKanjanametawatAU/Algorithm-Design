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
        self.index = None
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

    def precede(self, x):
        return self.g < x.g

    def assign(self, v):
        if self.g > v:
            self.g = v
            return True
        else:
            return False


def UFS(s):
    notSimplePQ = Priority_Queue()
    notSimplePQ.enqueue(s)
    Explored = [False for _ in range(V)]
    Explored[s.u] = True
    print("EnQueued: ", s.u, s.g)
    print(list(map(lambda x:(x.u,x.g), notSimplePQ.a)))

    while not notSimplePQ.empty():
        node = notSimplePQ.dequeue()
        Explored[node.u] = True

        if node.is_goal():
            return node.g, node

        for suc in node.successor():
            if not Explored[suc.u]:
                notSimplePQ.enqueue(suc)
                print("EnQueued: ", suc.u, suc.g)
                print(list(map(lambda x: (x.u, x.g), notSimplePQ.a)))
            else:
                notSimplePQ.elevate_key(suc, suc.g)
                print("Elevated: ", suc.u, suc.g)
                print(list(map(lambda x: (x.u, x.g), notSimplePQ.a)))


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