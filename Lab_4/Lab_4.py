import heapq
import random
import time
import matplotlib.pyplot as plt

# Dijkstra's Algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Floyd-Warshall Algorithm
def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {i: {j: float('inf') for j in nodes} for i in nodes}

    for i in nodes:
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = graph[i][j]

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Function to perform empirical analysis
def empirical_analysis(num_nodes, density):
    graph = generate_graph(num_nodes, density)

    # Dijkstra's Algorithm
    start_time = time.time()
    for i in range(num_nodes):
        dijkstra(graph, i)
    dijkstra_time = time.time() - start_time

    # Floyd-Warshall Algorithm
    start_time = time.time()
    floyd_warshall(graph)
    floyd_warshall_time = time.time() - start_time

    return dijkstra_time, floyd_warshall_time

# Function to generate a random graph
def generate_graph(num_nodes, density):
    graph = {}
    for i in range(num_nodes):
        graph[i] = {}
        for j in range(num_nodes):
            if i != j and random.random() < density:
                graph[i][j] = random.randint(1, 10)
    return graph

if __name__ == "__main__":
    num_nodes = 10
    sparse_density = 0.2
    dense_density = 0.8

    sparse_dijkstra_time, sparse_floyd_warshall_time = empirical_analysis(num_nodes, sparse_density)
    dense_dijkstra_time, dense_floyd_warshall_time = empirical_analysis(num_nodes, dense_density)

    print("Sparse Graph - Dijkstra's Time:", sparse_dijkstra_time)
    print("Sparse Graph - Floyd-Warshall's Time:", sparse_floyd_warshall_time)
    print("Dense Graph - Dijkstra's Time:", dense_dijkstra_time)
    print("Dense Graph - Floyd-Warshall's Time:", dense_floyd_warshall_time)

    # Additional: Increase Graph Size and Analyze
    num_nodes = [10, 20, 30, 40, 50]  # Example list of different graph sizes
    density = 0.5  # Example density for the graphs

    dijkstra_times = []
    floyd_warshall_times = []

    for n in num_nodes:
        dijkstra_time, floyd_warshall_time = empirical_analysis(n, density)
        dijkstra_times.append(dijkstra_time)
        floyd_warshall_times.append(floyd_warshall_time)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Plot Dijkstra's Algorithm
    plt.plot(num_nodes, dijkstra_times, label="Dijkstra", marker='o')

    # Plot Floyd-Warshall Algorithm
    plt.plot(num_nodes, floyd_warshall_times, label="Floyd-Warshall", marker='o')

    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (s)")
    plt.title("Algorithm Performance vs. Graph Size")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Additional: Increase Graph Size and Analyze
    num_nodes = [10, 20, 30, 40, 50]  # Example list of different graph sizes
    density = 0.5  # Example density for the graphs

    dijkstra_times = []
    floyd_warshall_times = []

    for n in num_nodes:
        dijkstra_time, _ = empirical_analysis(n, density)
        floyd_warshall_time, _ = empirical_analysis(n, density)
        dijkstra_times.append(dijkstra_time)
        floyd_warshall_times.append(floyd_warshall_time)

    # Plotting
    plt.figure(figsize=(12, 6))

    # Plot Dijkstra's Algorithm
    plt.subplot(1, 2, 1)
    plt.plot(num_nodes, dijkstra_times, label="Dijkstra", marker='o', color='blue')
    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (s)")
    plt.title("Dijkstra's Algorithm Performance vs. Graph Size")
    plt.grid(True)
    plt.legend()

    # Plot Floyd-Warshall Algorithm
    plt.subplot(1, 2, 2)
    plt.plot(num_nodes, floyd_warshall_times, label="Floyd-Warshall", marker='o', color='green')
    plt.xlabel("Number of Nodes")
    plt.ylabel("Execution Time (s)")
    plt.title("Floyd-Warshall Algorithm Performance vs. Graph Size")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
