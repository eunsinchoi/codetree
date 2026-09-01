N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
def recog_sign(num):
    if num < 0:
        sign = -1
    elif num > 0:
        sign = 1
    return sign


cnt = 0
max_cnt = 1

for i in range(N):
    if recog_sign(arr[i]) == recog_sign(arr[i-1]):
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)