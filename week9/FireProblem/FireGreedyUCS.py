class Priority_Queue:
    def __init__(self):
        self.a = []

    def empty(self):
        if self.a == []:
            return True
        else:
            return False

    def heapify(self, i):
        l = i * 2 + 1
        r = (i + 1) * 2
        if l < len(self.a) and not self.a[i].precede(self.a[l]):
            largest = l
        else:
            largest = i
        if r < len(self.a) and not self.a[largest].precede(self.a[r]):
            largest = r
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.a[i].index = i
            self.a[i].largest = largest
            self.heapify(largest)

    def enqueue(self, x):
        self.a.append(x)
        i = len(self.a) - 1
        self.a[i].index = i
        j = (i - 1) // 2
        while i > 0 and self.a[i].precede(self.a[j]):
            self.a[i], self.a[j] = self.a[j], self.a[i]
            self.a[i].index = i
            self.a[j].index = j
            i = j
            j = (i - 1) // 2

    def dequeue(self):
        x = self.a[0]
        i = len(self.a) - 1
        self.a[0], self.a[i] = self.a[i], self.a[0]
        self.a[0].index = 0
        self.a[i].index = i
        del self.a[i]
        self.heapify(0)
        return x

    def elevate_key(self, x, k):  # must increase priority of x
        if x.assign(k):
            i = x.index
            j = (i - 1) // 2
            while i > 0 and self.a[i].precede(self.a[j]):
                self.a[i], self.a[j] = self.a[j], self.a[i]
                self.a[i].index = i
                self.a[j].index = j
                i = j
                j = (i - 1) // 2


N = int(input())
House = []
for _ in range(N):
    House.append(list(map(int, input().split())))

Choice = [None for _ in range(2*N-1)]

Selection_List = []
for i in range(2*N-1):
    # print all positive number or zero number that add up to i
    sel = []
    for j in range(N):
        if i-j >= 0 and i-j < N:
            sel.append((i, House[j][i-j]))
    Selection_List.append(sel)

class state:
    def __init__(self, i, j, g):
        self.i = i
        self.j = j
        self.g = g
        self.index = None

    def precede(self, x):
        return self.j > x.j

    def assign(self, v):
        if self.g < v:
            self.g = v
            return True
        else:
            return False





PQ = Priority_Queue()
s = state(Selection_List[-1][0][0], Selection_List[-1][0][1] , House[N-1][N-1])
PQ.enqueue(s)
p = []
for i in range(2*N-2, 0, -1):
    u = PQ.dequeue()
    p.append(u)

    for v in Selection_List[i-1]:
        a = state(v[0], v[1], u.g + v[1])
        PQ.enqueue(a)

p = list(map(lambda a:(a.i, a.j), p))
p.reverse()
print(p)
print(sum(list(map(lambda a:a[1], p))))
