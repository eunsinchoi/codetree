x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
arr = [[0]*2001 for _ in range(2001)]

min_x = 2001
min_y = 2001
max_x = -1
max_y = -1


def check_box(arr, value, x1, x2, y1, y2):
    for dx in range(x2-x1):
        for dy in range(y2-y1):
            a = x1+1000 + dx
            b = y1+1000 + dy
            arr[a][b] = value


check_box(arr, 1, x1[0], x2[0], y1[0], y2[0])
check_box(arr, 0, x1[1], x2[1], y1[1], y2[1])

exist = False

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            exist = True
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)

if not exist:
    print(0)
else:
    print((max_x-min_x+1)*(max_y-min_y+1))