'''
Python 3
Each obj to be enqueued must be a class instance
A field called 'index' will be added

Two functions are required for class definition of queue's element (an object):
1) precede(self,x)
      returns True if the object precedes the object x
2) assign(self,v)
      assigns higher priority value v to the object's key
      returns True if the v is successfully assigned
      returns False if v has lower priority than object's key (not assigned)
'''

class Priority_Queue:
    def __init__(self):
        self.a = []
        
    def empty(self):
        if self.a == []:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < len(self.a) and not self.a[i].precede(self.a[l]):
            largest = l
        else:
            largest = i
        if r < len(self.a) and not self.a[largest].precede(self.a[r]):
            largest = r
        if largest != i:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.a[i].index = i
            self.a[i].largest = largest
            self.heapify(largest)
        
    def enqueue(self, x):
        self.a.append(x)
        i = len(self.a)-1
        self.a[i].index = i
        j = (i-1)//2
        while i > 0 and self.a[i].precede(self.a[j]):
            self.a[i],self.a[j] = self.a[j],self.a[i]
            self.a[i].index = i
            self.a[j].index = j
            i = j
            j = (i-1)//2

    def dequeue(self):
        x = self.a[0]
        i = len(self.a)-1
        self.a[0],self.a[i] = self.a[i],self.a[0]
        self.a[0].index = 0
        self.a[i].index = i
        del self.a[i]
        self.heapify(0)
        return x

    def elevate_key(self, x, k):  # must increase priority of x
        if x.assign(k):
            i = x.index
            j = (i-1)//2
            while i > 0 and self.a[i].precede(self.a[j]):
                self.a[i],self.a[j] = self.a[j],self.a[i]
                self.a[i].index = i
                self.a[j].index = j
                i = j
                j = (i-1)//2




        # Example class definition for queue's element and test code


# class MyClass:
#     def __init__(self, k):
#         self.key = k
#
#     def precede(self, x):
#         return self.key < x.key   # do not use <= or >=
#
#     def assign(self, v):  # v must be of higher priority value than the current key
#         x = MyClass(v)  # x is a local temporary instance
#         if not self.precede(x):
#             self.key = v
#             return True
#         else:
#             return False
#
# l = []
# for i in range(10):
#     l.append(MyClass(100-i))
#
# pq = Priority_Queue()
# for x in l:
#     pq.enqueue(x)
#
# print(95 in (map(lambda a:a.key, pq.a)))
#
# while not pq.empty():
#     print(pq.dequeue().key)

