n, m = map(int, input().split())

# Process A's movements
A = []
a_pos = 0
for _ in range(n):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        a_pos += vi
        A.append(a_pos)

# Process B's movements
B = []
b_pos = 0

for _ in range(m):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        b_pos += vi
        B.append(b_pos)

# Please write your code here.
diff = []
cnt = 0 

for t in range(len(A)):
    if A[t] > B[t]:
        diff.append('A')
    elif A[t] < B[t]:
        diff.append('B')
    elif A[t] == B[t]:
        if t==0:
            diff.append('N')
        else: diff.append(diff[t-1])

for i in range(1, len(diff)):
    if (diff[i-1] != 'N') and (diff[i] != diff[i-1]):
        cnt += 1

print(cnt)