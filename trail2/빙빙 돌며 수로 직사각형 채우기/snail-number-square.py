n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

#우하좌상
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_n = 0

# Please write your code here.
pos = [0, 0]

for num in range(1, n*m+1):
    arr[pos[0]][pos[1]] = num
    # print(arr[pos[0]][pos[1]])
    sus_pos_0 = pos[0] + dir[dir_n][0]
    sus_pos_1 = pos[1] + dir[dir_n][1]
    if (sus_pos_0 not in range(n)) or (sus_pos_1 not in range(m)) or (arr[sus_pos_0][sus_pos_1]!= 0):
        dir_n = (dir_n +1)%4

    pos[0] += dir[dir_n][0]
    pos[1] += dir[dir_n][1]
    # print(pos)

for row in arr:
    for i in range(len(row)):
        print(row[i], end=' ')
    print()