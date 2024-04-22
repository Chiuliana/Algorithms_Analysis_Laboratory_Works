from collections import defaultdict, deque

class Graph_BFS:
    def __init__(self):
        self.adjList = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)  # If the graph is undirected, add this line

    def bfs(self, startNode):
        # Create a queue for BFS
        queue = deque()
        max_node = max(self.adjList.keys(), default=-1)  # Get the maximum node value
        visited = [False] * (max_node + 1)  # Initialize the visited list

        visited[startNode] = True
        queue.append(startNode)

        while queue:
            # Dequeue a vertex from queue and print it
            currentNode = queue.popleft()
            for neighbor in self.adjList[currentNode]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
