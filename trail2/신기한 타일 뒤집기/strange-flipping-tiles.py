n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

pos = 0
color = {}

for num, direction in commands:
    num = int(num)

    if direction == 'R':
        sign = 1
    elif direction == 'L':
        sign = -1

    for i in range(num):
        color[pos+i*sign] = direction
    pos = pos + (num-1)*sign


colors = list(color.values())
print(f"{colors.count('L')} {colors.count('R')}")