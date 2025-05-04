import heapq

def prims_algorithm(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        total_cost += cost

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor))

    return total_cost

# Take input from user
def build_graph():
    graph = {}
    n = int(input("Enter number of edges: "))
    print("Enter edges in format: node1 node2 weight")
    for _ in range(n):
        u, v, w = input().split()
        w = int(w)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))  # Because it's an undirected graph
    return graph

graph = build_graph()
start_node = input("Enter starting node: ")
mst_cost = prims_algorithm(graph, start_node)
print("Minimum cost of MST:", mst_cost)
