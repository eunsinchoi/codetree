n, t = map(int, input().split())
x, y, d = input().split()
x, y = int(x), int(y)

# Please write your code here.
# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

mapper = {
    'U' : 3,
    'D' : 1,
    'R' : 0,
    'L' : 2,
}

face = mapper[d]
# print(d, face)
# print(f"초기 x y {x, y}")

for _ in range(t):
    if (x+dx[face] in range(1, n+1)) and (y+dy[face] in range(1, n+1)):
        x += dx[face]
        y += dy[face]
        # print('이동', face, x, y)
    else: 
        face = (face+2)%4
        # print('방향', face, x, y)


print(x, y)