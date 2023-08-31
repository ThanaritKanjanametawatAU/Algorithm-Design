from disjointsets3 import DisjointSets
V, E = map(int, input().split())
Edges = [tuple(map(int, input().split())) for _ in range(E)]

def Kruskal(V, Edges):
    Edges = sorted(Edges, key=lambda x: x[2])

    # Create Disjoint Set
    D = DisjointSets(V)

    W = 0
    edgecount = 0

    for u, v, w in Edges:
        if D.findset(u) != D.findset(v):
            D.union(u, v)
            print(u, v, w)
            W += w
            edgecount += 1

    print(W)

Kruskal(V, Edges)