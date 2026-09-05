n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
grid = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

for edge in edges:
    grid[edge[0]][edge[1]] += 1
    grid[edge[1]][edge[0]] += 1

# print(grid)


nodes = []
def search_nodes(grid, n, start):
    visited[start] = True

    for i in range(n+1):
        if grid[start][i] > 0 and not visited[i]:
            nodes.append(i)
            search_nodes(grid, n, i)
    return nodes
    
print(len(search_nodes(grid, n, 1)))