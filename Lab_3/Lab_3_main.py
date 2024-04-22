import time
import matplotlib.pyplot as plt
import pandas as pd

from Lab_3_DFS import Graph_DFS
from Lab_3_BFS import Graph_BFS

def generate_input_data(size):
    graph = Graph_DFS()  # Using Graph_DFS for DFS analysis
    for i in range(size - 1):
        graph.addEdge(i, i + 1)
    return graph

def measure_execution_time(algorithm, graph):
    start_time = time.time()
    if algorithm == 'DFS':
        graph.DFS(0)  # Start DFS from vertex 0
    elif algorithm == 'BFS':
        bfs_graph = Graph_BFS()  # Using Graph_BFS for BFS analysis
        for u, neighbors in graph.graph.items():
            for v in neighbors:
                bfs_graph.addEdge(u, v)
        bfs_graph.bfs(0)  # Start BFS from vertex 0
    return time.time() - start_time

def main():
    values = [10, 50, 100, 200, 300, 400, 500]
    timeDFS = []
    timeBFS = []

    for i in values:
        graph = generate_input_data(i)

        # Measure execution time for DFS
        start_time_dfs = time.time()
        graph.DFS(0)
        end_time_dfs = time.time()
        timeDFS.append(end_time_dfs - start_time_dfs)

        # Measure execution time for BFS
        start_time_bfs = time.time()
        bfs_graph = Graph_BFS()  # Using Graph_BFS for BFS analysis
        for u, neighbors in graph.graph.items():
            for v in neighbors:
                bfs_graph.addEdge(u, v)
        bfs_graph.bfs(0)
        end_time_bfs = time.time()
        timeBFS.append(end_time_bfs - start_time_bfs)

    plt.plot(values, timeDFS, label="Depth First Search")
    plt.xlabel('Number of nodes')
    plt.ylabel('Time')
    plt.title('Execution Time for DFS')
    plt.legend()
    plt.show()

    plt.plot(values, timeBFS, label="Breadth First Search")
    plt.xlabel('Number of nodes')
    plt.ylabel('Time')
    plt.title('Execution Time for BFS')
    plt.legend()
    plt.show()

    plt.plot(values, timeDFS, label="Depth First Search")
    plt.plot(values, timeBFS, label="Breadth First Search")
    plt.xlabel('Number of nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Graph Traversal Algorithms')
    plt.legend()  # Adding legend
    plt.show()

    data = []
    for i in range(len(values)):
        n = values[i]
        data.append([n, timeDFS[i], timeBFS[i]])

    # Display results in a table
    headers = ["Input Size", 'DFS', 'BFS']
    df = pd.DataFrame(data, columns=headers)
    print(df)

if __name__ == "__main__":
    main()
