
def bfs_shortest_path(maze, start, goal):
    queue = [(start, [start])]
    visited = [start]
    explored = 0
    while len(queue) > 0:
        (r, c), path = queue.pop(0)
        explored += 1
        if (r, c) == goal:
            return path, explored
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 1 and (nr, nc) not in visited):
                visited.append((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None, explored
def dfs_path(maze, start, goal):
    stack = [(start, [start])]
    visited = []
    explored = 0
    while len(stack) > 0:
        (r, c), path = stack.pop()
        explored += 1
        if (r, c) == goal:
            return path, explored
        if (r, c) in visited:
            continue
        visited.append((r, c))
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] == 1 and (nr, nc) not in visited):
                stack.append(((nr, nc), path + [(nr, nc)]))
    return None, explored
maze = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 1, 1, 1]
]
start = (0, 0)
goal = (2,2)
bfs_res, bfs_exp = bfs_shortest_path(maze, start, goal)
dfs_res, dfs_exp = dfs_path(maze, start, goal)
print("BFS Shortest Path:", bfs_res)
print("Nodes Explored by BFS:", bfs_exp)
print("\nDFS Path:", dfs_res)
print("Nodes Explored by DFS:", dfs_exp)
print("\nComparison:")
print("BFS explored:", bfs_exp, "nodes")
print("DFS explored:", dfs_exp, "nodes")