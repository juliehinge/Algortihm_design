import math
from collections import defaultdict, deque



def process_test_case():


	# Number of gohers and wholes, and time limit and velocity of the gophers
	n_gophers, m_holes, s_seconds, v_velocity = map(int, input().split())

	# Appending each of the gopher coordinates to a list
	gophers_coordinates = []
	for i in range(n_gophers):
	    gophers_coordinates.append(list(map(float, input().split())))

	# Appending each of the hole coordinates to a list
	holes_coordinates = []
	for i in range(m_holes):
	    holes_coordinates.append(list(map(float, input().split())))




	def distance_calc(gopher, hole):
	    return math.sqrt((hole[0] - gopher[0])**2 + (hole[1] - gopher[1])**2)

	gopher_distance = v_velocity * s_seconds

	# Bipartite graph representation
	g = defaultdict(list)

	for gopher_idx, gopher in enumerate(gophers_coordinates):
	    for hole_idx, hole in enumerate(holes_coordinates):
	        distance = distance_calc(gopher, hole)
	        if distance <= gopher_distance:
	            g[gopher_idx].append(n_gophers + hole_idx) 

	# BFS to set levels to vertices
	def BFS(match, dist):
	    queue = deque()
	    for i in range(n_gophers):
	        if match[i] == -1:
	            dist[i] = 0
	            queue.append(i)
	        else:
	            dist[i] = float('inf')
	    dist[-1] = float('inf')

	    while queue:
	        u = queue.popleft()
	        if u != -1:
	            for v in g[u]:
	                if dist[match[v]] == float('inf'):
	                    dist[match[v]] = dist[u] + 1
	                    queue.append(match[v])
	    return dist[-1] != float('inf')

	# DFS to find possible bipartite match
	def DFS(u, match, dist):
	    if u == -1:
	        return True
	    for v in g[u]:
	        if dist[match[v]] == dist[u] + 1 and DFS(match[v], match, dist):
	            match[v] = u
	            match[u] = v
	            return True
	    dist[u] = float('inf')
	    return False

	# Hopcroft-Karp for maximum bipartite matching
	def HopcroftKarp():
	    match = [-1] * (n_gophers + m_holes)
	    dist = [-1] * (n_gophers + m_holes)
	    matching = 0
	    while BFS(match, dist):
	        for i in range(n_gophers):
	            if match[i] == -1 and DFS(i, match, dist):
	                matching += 1
	    return matching

	print(n_gophers - HopcroftKarp())




# To handle multiple test cases
while True:
    try:
        process_test_case()
    except EOFError:
        break





