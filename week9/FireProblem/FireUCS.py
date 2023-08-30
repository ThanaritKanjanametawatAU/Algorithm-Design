from week9.FireProblem.module.notSimplePriorityQueue import *
N = int(input())
House = []
for _ in range(N):
    House.append(list(map(int, input().split())))

Choice = [None for _ in range(2*N-1)]

def valid(i, j, depth):
    return i >= 0 and i < N and j >= 0 and j < N and i+j > depth


class state:
    def __init__(self, i, j, g):
        self.i = i
        self.j = j
        self.g = g
        self.depth = 0
        self.index = None
        self.parent = None

    def successor(self):
        result = []
        visited = self.getParents()
        for i in range(N):
            for j in range(N):
                if valid(i, j, self.depth) and (i, j) not in visited and (i, j) != (self.i, self.j):
                    a = state(i, j, self.g + House[i][j])
                    a.depth = self.depth + 1
                    a.parent = self
                    result.append(a)


        return result

    def getParents(self):
        parents = []
        current = self
        while current.parent != None:
            parents.append((current.parent.i, current.parent.j))
            current = current.parent
        return parents


    def is_goal(self):
        return self.depth == 2*N - 2

    def precede(self, x):
        return self.g > x.g
    # def precede(self, x):
    #     return self.depth>x.depth

    def assign(self, v):
        if self.g < v:
            self.g = v
            return True
        else:
            return False


def UFS(s):
    notSimplePQ = Priority_Queue()

    notSimplePQ.enqueue(s)
    goals = []
    i = 0
    maxCost = -1

    while not notSimplePQ.empty():
        node = notSimplePQ.dequeue()
        # print(node.depth, "-", node.i, node.j, node.g)

        if node.is_goal():
            maxCost = max(maxCost, node.g)

        for suc in node.successor():
            # print("EnQueued: ", suc.depth, "-", suc.i, suc.j, suc.g)
            notSimplePQ.enqueue(suc)

    return maxCost

s = state(0, 0, 0)
# print(s.successor()[-1].successor()[-1].i, s.successor()[-1].successor()[-1].j)
# print(s.successor()[-1].successor()[-1].getParents())
# print(len(s.successor()[-1].successor()[-1].successor()))

print(list(map(lambda x: (x.i, x.j), s.successor())))
maxCost = UFS(s)
print(maxCost)


# FireWall = [[0 for _ in range(N)] for _ in range(N)]
# FireCount = 4
# def generateFire(FireWall, FireCount):
#     for fc in range(FireCount+1):
#         i = 0
#         while i <= fc:
#             FireWall[i][fc-i] = 1
#             i += 1



# def getPath(s):
#     # s is goal returned from UFS
#     path = []
#     pathij = []
#     while s != None:
#         path.insert(0, s.g)
#         pathij.insert(0, (s.i, s.j))
#         s = s.parent
#     return path, pathij
#
# path, pathij = getPath(goal)
#
# print(cost)
# for i in range(len(path)-1):
#     print(path[i], end='->')
# print(path[-1])
#
# for i in range(1, len(path)):
#     print(path[i] - path[i-1], end=' ')
#
# print()
# for i in range(len(pathij)):
#     print(pathij[i], end='->')