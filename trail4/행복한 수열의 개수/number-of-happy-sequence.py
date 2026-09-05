n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def count_happy(grid, n, m):
    cnt = 0
    if not m == 1:
        for row in grid:
            row_cnt = 0
            for i in range(n-m+1):
                if all(row[i+t] == row[i+t+1] for t in range(m-1)):
                    row_cnt+=1
            if row_cnt > 0:
                cnt += 1
    else:
        cnt = n
    return cnt

grid_T = list(map(list, zip(*grid)))
# print(count_happy(grid, n, m))
# print(count_happy(grid_T, n, m))

total = count_happy(grid, n, m) + count_happy(grid_T, n, m)

print(total)