#BFS method to traverse graph

def bfs(graph, start):
    path = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:
            path.append(vertex)
            queue.extend(graph[vertex])
    return path


test_graph = {
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['C', 'G'],
    'G': ['F', 'S'],
    'H': ['E', 'G'],
    'S': ['A', 'C', 'G']
}
print(bfs(test_graph, 'A'))