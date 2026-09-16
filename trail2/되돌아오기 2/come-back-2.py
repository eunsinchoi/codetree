commands = input()

# Please write your code here.
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
x = 0
y = 0
time = 0
found = False

for i in commands:
    
    if i == 'L':
        d -= 1
        d = d%4
        time += 1
    elif i == 'R':
        d += 1
        d = d%4
        time += 1
    else:
        x += dx[d]
        y += dy[d]
        time += 1
        if x == 0 and y == 0:
            print(time)
            break
    
    
else:
    print(-1)
