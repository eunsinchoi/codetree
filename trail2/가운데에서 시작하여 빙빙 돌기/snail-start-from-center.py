n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
pos_x = n//2  # 2
pos_y = n//2  # 2

#우상좌하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
d = 3  # 방향 인덱스

for i in range(1, n*n+1):
    grid[pos_x][pos_y] = i

    if (0<=pos_x+dx[d]<n) and (0<=pos_y+dy[d]<n):
        if grid[pos_x+dx[(d+1)%4]][pos_y+dy[(d+1)%4]] == 0:
            d = (d+1)%4
    else:
        d = (d+1)%4
    
    pos_x += dx[d]
    pos_y += dy[d]

for row in grid:
    print(*row)