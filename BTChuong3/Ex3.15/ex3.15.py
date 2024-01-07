import math

class Graph_num7:
    def __init__(self, size):
        self.size = size
        self.table = None
        
        
g  = Graph_num7(9) 
g.table = [[1, 4, 1, 1, 1, 1, 1, 8, 1], 
           [4, 1, 8, 1, 1, 1, 1, 11, 1], 
           [1, 8, 1, 7, 1, 4, 1, 1, 2], 
           [1, 1, 7, 1, 9, 14, 1, 1, 1], 
           [1, 1, 1, 9, 1, 11, 1, 1, 1], 
           [1, 1, 4, 14, 11, 1, 2, 1, 1], 
           [1, 1, 1, 1, 1, 2, 1, 1, 6], 
           [8, 11, 1, 1, 1, 1, 1, 1, 7], 
           [1, 1, 2, 1, 1, 1, 6, 7, 1]]

# Algoritmus ma zlozitost O(V^2) !!

def minDistance(graph, distance, shortestTree):
    m1 = math.inf
    for v in range(graph.size):
        if distance[v] < m1 and shortestTree[v] == False:
            m1 = distance[v]
            sonhonhat = v
    return sonhonhat

def Dijkstra(graph, src_vertex):
    distance = [math.inf] * graph.size
    distance[src_vertex] = 0
    shortestTree = [False] * graph.size

    for i in range(graph.size):
        u = minDistance(graph, distance, shortestTree)

        shortestTree[u] = True

        for ver in range(graph.size):
            weight = graph.table[u][ver]
            if weight > 0 and shortestTree[ver] == False and distance[ver] > distance[u] + weight:
                distance[ver] = distance[u] + weight
    print("Vertex tDistance from Source")
    for n in range(graph.size):
        print(n, distance[n])

Dijkstra(g, 0)