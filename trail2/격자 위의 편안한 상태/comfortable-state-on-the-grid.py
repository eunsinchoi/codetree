n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# Please write your code here.
for _ in range(m):
    x, y = [a-1 for a in map(int, input().split())]
    arr[x][y] = 1
    nearby = 0
    for i in range(4):
        if 0 <= x+dx[i] <= n-1 and 0 <= y+dy[i] <= n-1:
            nearby += arr[x+dx[i]][y+dy[i]]

    if nearby == 3:
        print(1)
    else:
        print(0)