direction = {
    'W' : (0, -1),
    'S' : (1, 0),
    'N' : (-1, 0),
    'E' : (0, 1)
}

x = 0
y = 0
time = 0
found = False

for i in range(int(input())):
    d, l = input().split()
    for _ in range(int(l)):
        time += 1
        x += direction[d][0]
        y += direction[d][1]
        # print(x, y)
        if x == 0 and y == 0:
            print(time)
            found = True
            break
    if found:
        break
else:
    print(-1)