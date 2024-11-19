class Graph:
    def __init__(self):
        self.graph = {}  

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)

    def display_graph(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {edges}")

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            current = queue.pop(0)
            print(current, end=" ")
            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


def main():
    g = Graph()
    while True:
        print("\nOptions:")
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Display Graph")
        print("4. Perform DFS")
        print("5. Perform BFS")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            vertex = input("Enter vertex: ")
            g.add_vertex(vertex)
            print(f"Vertex '{vertex}' added.")

        elif choice == "2":
            vertex1 = input("Enter the starting vertex: ")
            vertex2 = input("Enter the ending vertex: ")
            g.add_edge(vertex1, vertex2)
            print(f"Edge '{vertex1} -> {vertex2}' added.")

        elif choice == "3":
            print("\nGraph:")
            g.display_graph()

        elif choice == "4":
            start = input("Enter the starting vertex for DFS: ")
            print("\nDFS Traversal:")
            g.dfs(start)
            print()  

        elif choice == "5":
            start = input("Enter the starting vertex for BFS: ")
            print("\nBFS Traversal:")
            g.bfs(start)
            print()  

        elif choice == "6":
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()