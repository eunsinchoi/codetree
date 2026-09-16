N, M = map(int, input().split())

a = []
pos = 0
for _ in range(N):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        pos += vi
        a.append(pos)

b = []
pos = 0
for _ in range(M):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        pos += vi
        b.append(pos)

head = []
for i in range(len(a)):
    if a[i] > b[i]:
        head.append(0)
    elif b[i] > a[i]:
        head.append(1)
    else:
        head.append(2)

cnt = 0
for i in range(len(head)):
    if i == 0 or head[i-1]!=head[i]:
        cnt += 1
print(cnt)