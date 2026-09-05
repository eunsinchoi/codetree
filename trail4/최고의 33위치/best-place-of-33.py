n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
sum_value = []

for x in range(n-2):
    for y in range(n-2):
        a = 0
        # print(x)
        for i in range(x, x+3):
            for j in range(y, y+3):
                # print(i, j)
                a += grid[i][j]
        sum_value.append(a)

print(max(sum_value))