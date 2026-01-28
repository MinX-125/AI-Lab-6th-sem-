import numpy as np
from collections import deque
import matplotlib.pyplot as plt
def bfs_maze(rows, cols):
    maze=np.array([
        [1,1,0,0,1,1],
        [0,1,0,1,1,0],
        [1,1,1,1,0,0],
        [1,0,0,1,1,0]
    ])
    print("\nMaze:")
    print_maze(maze)
    start=(3,0)
    end=(0,5)
    frontier=deque([start])
    visited=[start]
    traversed=[]
    parent={}
    moves=[(1,0),(-1,0),(0,1),(0,-1)]
    while frontier:
        current=frontier.popleft()
        traversed.append(current)
        if current==end:
            break
        x,y=current
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if 0<=nx<rows and 0<=ny< cols:
                if maze[nx,ny]==1 and (nx,ny) not in visited:
                    frontier.append((nx,ny))
                    visited.append((nx,ny))
                    parent[(nx,ny)]=(x,y)
    if end not in visited:
        print("\nNo path found!")
        return 0
    path=[]
    step=end
    while step!=start:
        path.append(step)
        step=parent[step]
    path.append(start)
    path.reverse()
    print("\nBFS Path Found:", path)
    print("BFS Nodes Explored:", len(traversed))
    plt.imshow(maze,cmap="gray_r")
    px,py=zip(*path)
    plt.plot(py,px,c='red',linewidth=3)
    plt.scatter(start[1],start[0],c='cyan',s=80)
    plt.scatter(end[1],end[0],c='pink',s=80)
    plt.title("BFS Path")
    plt.show()
    return len(traversed)

def dfs_maze(rows, cols):
    maze=np.array([
        [1,1,0,0,1,1],
        [0,1,0,1,1,0],
        [1,1,1,1,0,0],
        [1,0,0,1,1,0]
    ])
    start=(3,0)
    end=(0,5)
    stack=[start]
    visited=set()
    parent={}
    traversed=[]
    moves=[(1,0),(-1,0),(0,1),(0,-1)]
    while stack:
        current=stack.pop()
        if current in visited:
            continue
        visited.add(current)
        traversed.append(current)
        if current==end:
            break
        x,y=current
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols:
                if maze[nx,ny]==1 and (nx,ny) not in visited:
                    stack.append((nx,ny))
                    parent[(nx,ny)] = current
    if end not in visited:
        print("\nDFS: No path found!")
        return 0
    path=[]
    step=end
    while step!=start:
        path.append(step)
        step=parent[step]
    path.append(start)
    path.reverse()
    print("\nDFS Path Found:", path)
    print("DFS Nodes Explored:", len(traversed))
    plt.imshow(maze,cmap="gray_r")
    px,py=zip(*path)
    plt.plot(py,px,c='blue',linewidth=3)
    plt.scatter(start[1],start[0],c='cyan',s=80)
    plt.scatter(end[1],end[0],c='pink',s=80)
    plt.title("DFS Path")
    plt.show()
    return len(traversed)

def print_maze(maze):
    for row in maze:
        print("".join(['1' if cell==1 else '█' for cell in row]))

bfs_nodes = bfs_maze(4,6)
dfs_nodes = dfs_maze(4,6)
print("\nComparison:")
print("BFS Nodes Explored:", bfs_nodes)
print("DFS Nodes Explored:", dfs_nodes)
if bfs_nodes<dfs_nodes:
    print("BFS is better for the given maze.")
elif bfs_nodes>dfs_nodes:
    print("DFS is better for the given maze.")
else:
    print("BFS and DFS are equally good for the given maze.")