n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
#좌상우하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

#'/'이면 +1 '\\'이면 -1


x = 0
y = 0
h = 2
for a in range(1, k):
    if a%n == 0:
        h = (h+1)%4

    else:
        x += dx[h]
        y += dy[h]
h = (h+1)%4

cnt = 1
# print(x, y)
while True:
    if grid[x][y] == '/':
        a = [0,3]
        b = [1,2]
        if h in a:
            i = a.index(h)
            h = a[(i+1)%2]
        else:
            i = b.index(h)
            h = b[(i+1)%2]

    else:
        a = [0,1]
        b = [2,3]
        if h in a:
            i = a.index(h)
            h = a[(i+1)%2]
        else:
            i = b.index(h)
            h = b[(i+1)%2]
    
    x += dx[h]
    y += dy[h]
    # print(x, y)

    if (0 <= x < n) and (0 <= y < n):
        cnt += 1
    else:
        print(cnt)
        break