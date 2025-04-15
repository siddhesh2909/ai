import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def get_input():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for _ in range(num_nodes):
        node = input(f"Enter node: ").strip()
        graph[node] = {}

        num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))
        for _ in range(num_neighbors):
            neighbor, weight = input(f"Enter neighbor and weight: ").split()
            graph[node][neighbor] = int(weight)

    start_node = input("Enter the source node: ").strip()
    return graph, start_node

graph, start_node = get_input()

shortest_paths = dijkstra(graph, start_node)

print(f"\nShortest paths from {start_node}:")
for node, distance in shortest_paths.items():
    print(f"  To {node}: {distance}")
