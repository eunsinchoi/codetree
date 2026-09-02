S = input()


# Please write your code here.
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = 3
x = 0
y = 0

for i in S:
    if i == 'R':
        d = (d+1)%4
        # print(d, end='')
    elif i == 'L':
        d = (d-1)%4
        # print(d, end='')
    
    elif i == 'F':
        # print(dir[d])
        x += dir[d][0]
        y += dir[d][1]

print(x, y)
