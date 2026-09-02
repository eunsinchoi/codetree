N, M, K = map(int, input().split())
_list = [int(input()) for _ in range(M)]

# Please write your code here.
student = [0]*N


for i in _list:
    student[i-1] += 1
    if student[i-1] == K:
        print(i)
        break
else:
    print(-1) 

