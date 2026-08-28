n = int(input())
commands = [tuple(input().split()) for _ in range(n)]


# Please write your code here.
pos = 0
colored = {}

for x, dir in commands:
    x = int(x)

    if dir == 'R':
        dir_sign = 1
        color = 'b'
    elif dir == 'L':
        dir_sign = -1
        color = 'w'

    for i in range(x):
        if pos+(i*dir_sign) not in colored:
            colored[pos+(i*dir_sign)] = []
        colored[pos+(i*dir_sign)].append(color)

    pos += (x-1)*dir_sign


tile = []
for value in colored.values():
    if value.count('b')>=2 and value.count('w')>=2:
        tile.append('g')
    else:
        tile.append(value[-1])



print(f"{tile.count('w')} {tile.count('b')} {tile.count('g')}")