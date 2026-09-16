N = int(input())
arr = [[0]*201 for _ in range(201)]


for n in range(N):
    x1, y1, x2, y2 = [z+100 for z in map(int, input().split())]
    # print(x1, y1, x2, y2)
    
       
    for i in range(x1, x2):
        for j in range(y1, y2):
            if n%2 == 0:
                arr[i][j] = 1
                # print(arr[i][j])
            else:
                arr[i][j] = 2
                # print(arr[i][j])


cnt = 0
for row in arr:
    cnt += row.count(2)

print(cnt)