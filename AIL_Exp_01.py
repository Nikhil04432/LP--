def bfs(visited, graph, node):
    visited.append(node)
    queue = [node]

    print("BFS Traversal:", end=" ")
    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()  # For newline


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def main():
    graph = {}
    n = int(input("Enter number of nodes: "))
    print("Enter nodes and their neighbors:")
    for _ in range(n):
        node = input("Enter node name: ")
        edges = input(f"Enter neighbors of {node} separated by : ").split()
        graph[node] = edges

    start_node = input("Enter starting node for BFS and DFS: ")

    # Run BFS
    bfs_visited = []
    bfs(bfs_visited, graph, start_node)

    # Run DFS
    dfs_visited = []
    print("DFS Traversal:", end=" ")
    dfs(dfs_visited, graph, start_node)
    print()  # For newline


if __name__ == "__main__":
    main()
