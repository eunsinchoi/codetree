n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]

# Please write your code here.
x = 0
y = 0

#하우상좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

head = 0
visited = []

for i in range(1, n*m+1):
    arr[x][y] = i
    visited.append((x, y))

    if (not (0 <= x+dx[head] < n and 0 <= y+dy[head] < m)) or ((x+dx[head], y+dy[head]) in visited):
        head = (head+1)%4

    x += dx[head]
    y += dy[head]
      
    # print(x, y, head)
    # print(arr[x][y])


for a in range(n):
    print(*arr[a])
    