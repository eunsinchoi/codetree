N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 0

pos_x = N//2
pos_y = N//2

answer = board[pos_x][pos_y]

for i in str:
    if i == 'R':
        d = (d+1)%4
    elif i == 'L':
        d = (d-1)%4
    else:
        if 0<=pos_x+dx[d]<N and 0<=pos_y+dy[d]<N:
            pos_x += dx[d]
            pos_y += dy[d]
            answer += board[pos_x][pos_y]

print(answer)