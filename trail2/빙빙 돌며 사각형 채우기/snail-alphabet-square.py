n, m = map(int, input().split())

# Please write your code here.
arr = [[0]*m for _ in range(n)]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # len 26


#우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


pos_x = 0
pos_y = 0
d = 0

for i in range(n*m):
    arr[pos_x][pos_y] = alphabet[i%26]
    
    if (not 0<=pos_x+dx[d]<n) or (not 0<=pos_y+dy[d]<m) or (arr[pos_x+dx[d]][pos_y+dy[d]] != 0):
        d = (d+1)%4
    
    pos_x += dx[d]
    pos_y += dy[d]


for row in arr:
    print(*row)