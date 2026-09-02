n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

cnt = 0

for i in range(n):
    for j in range(n):
        ij = 0
        for k in range(4):
            if (i+x[k] in range(n)) and (j+y[k] in range(n)):
                ij += grid[i+x[k]][j+y[k]]
        if ij >= 3:
            cnt += 1

print(cnt)