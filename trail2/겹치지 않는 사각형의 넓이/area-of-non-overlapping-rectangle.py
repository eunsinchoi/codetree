arr = [[0] * 2001 for _ in range(2001)]

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for dx in range(x2-x1):
        for dy in range(y2-y1):
            x = x1+1000 + dx
            y = y1+1000 + dy
            arr[x][y]=1

mx1, my1, mx2, my2 = map(int, input().split())
for dx in range(mx2-mx1):
    for dy in range(my2-my1):
        x = mx1+1000 + dx
        y = my1+1000 + dy
        arr[x][y]=0

print(sum(row.count(1) for row in arr))