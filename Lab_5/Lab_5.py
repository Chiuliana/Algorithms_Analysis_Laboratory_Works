import heapq
import time
import random
import matplotlib.pyplot as plt

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def prim(graph):
    min_span_tree = []
    visited = set()
    start_node = next(iter(graph))
    visited.add(start_node)
    edges = [(cost, start_node, node) for node, cost in graph[start_node]]
    heapq.heapify(edges)

    while edges:
        cost, src, dest = heapq.heappop(edges)
        if dest not in visited:
            visited.add(dest)
            min_span_tree.append((src, dest, cost))
            for node, cost in graph[dest]:
                if node not in visited:
                    heapq.heappush(edges, (cost, dest, node))

    return min_span_tree

def kruskal(graph):
    min_span_tree = []
    edges = [(cost, src, dest) for src in graph for dest, cost in graph[src]]
    edges.sort()
    disjoint_set = DisjointSet(len(graph))

    for cost, src, dest in edges:
        if disjoint_set.find(src) != disjoint_set.find(dest):
            min_span_tree.append((src, dest, cost))
            disjoint_set.union(src, dest)

    return min_span_tree

def generate_random_graph(n, max_weight=100):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):
            weight = random.randint(1, max_weight)
            graph[i].append((j, weight))
            graph[j].append((i, weight))
    return graph

def measure_runtime(algorithm, graph):
    start_time = time.time()
    algorithm(graph)
    end_time = time.time()
    return end_time - start_time


def empirical_analysis():
    sizes = [10, 20, 30, 40, 50]
    prim_runtimes = []
    kruskal_runtimes = []

    for size in sizes:
        graph = generate_random_graph(size)

        prim_start_time = time.time()
        prim(graph)
        prim_end_time = time.time()
        prim_runtime = prim_end_time - prim_start_time
        prim_runtimes.append(prim_runtime)

        kruskal_start_time = time.time()
        kruskal(graph)
        kruskal_end_time = time.time()
        kruskal_runtime = kruskal_end_time - kruskal_start_time
        kruskal_runtimes.append(kruskal_runtime)

        print(
            f"Size: {size}, Prim's Runtime: {prim_runtime:.6f} seconds, Kruskal's Runtime: {kruskal_runtime:.6f} seconds")

    return sizes, prim_runtimes, kruskal_runtimes


def plot_graph(sizes, prim_runtimes, kruskal_runtimes):
    plt.plot(sizes, prim_runtimes, label="Prim's Algorithm")
    plt.plot(sizes, kruskal_runtimes, label="Kruskal's Algorithm")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Runtime (seconds)")
    plt.title("Empirical Analysis of Prim's and Kruskal's Algorithms")
    plt.legend()
    plt.show()

    plt.plot(sizes, prim_runtimes, label="Prim's Algorithm")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Runtime (seconds)")
    plt.title("Empirical Analysis of Prim's Algorithm")
    plt.legend()
    plt.show()

    plt.plot(sizes, kruskal_runtimes, label="Kruskal's Algorithm", color='orange')
    plt.xlabel("Number of Nodes")
    plt.ylabel("Runtime (seconds)")
    plt.title("Empirical Analysis of Kruskal's Algorithm")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    sizes, prim_runtimes, kruskal_runtimes = empirical_analysis()
    plot_graph(sizes, prim_runtimes, kruskal_runtimes)

