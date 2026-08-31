n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)
# print(x, y)

# Please write your code here.
arr = [[0]*201 for _ in range(201)]

for i in range(n):
    # print(i)
    for r in range(8):
        for l in range(8):
            a = x[i]+100+r
            b = y[i]+100+l
            # print(a, b)
            arr[a][b] = 1

print(sum(sum(row) for row in arr))