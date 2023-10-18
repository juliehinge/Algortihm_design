from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.capacities = {}

    def addEdge(self, u, v, w=1):
        self.graph[u].append(v)
        self.graph[v].append(u)  # for the back edges
        self.capacities[(u, v)] = w
        # Ensure the back edge exists in the capacities dictionary
        if (v, u) not in self.capacities:
            self.capacities[(v, u)] = 0

    def BFS(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[val] == False and self.capacities[(u, val)] > 0:
                    queue.append(val)
                    visited[val] = True
                    parent[val] = u
        return visited[t]

    def fordFulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.capacities[(parent[s], s)])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.capacities[(u, v)] -= path_flow
                self.capacities[(v, u)] += path_flow
                v = parent[v]
        return max_flow

n_children, m_toys, p_cat = map(int, input().split())
V = n_children + m_toys + p_cat + 2
g = Graph(V)

source = 0
sink = V - 1

# Connect source to all children
for i in range(1, n_children + 1):
    g.addEdge(source, i)

toy_start = n_children + 1
category_start = toy_start + m_toys

for i in range(1, n_children + 1):
    toys = list(map(int, input().split()))[1:]
    for toy in toys:
        g.addEdge(i, toy_start + toy - 1)

toy_categories = {}
category_limits = {}
for i in range(p_cat):
    line = list(map(int, input().split()))
    toys_in_category = line[1:-1]
    limit = line[-1]
    category_node = category_start + i
    category_limits[category_node] = limit
    for toy in toys_in_category:
        toy_categories[toy] = category_node
        g.addEdge(toy_start + toy - 1, category_node)
        g.capacities[(category_node, toy_start + toy - 1)] = 0  # No backflow from category to toy
    g.addEdge(category_node, sink, limit)

# For toys not in a category, connect them directly to sink
for i in range(1, m_toys + 1):
    if i not in toy_categories:
        g.addEdge(toy_start + i - 1, sink)

print(g.fordFulkerson(source, sink))
