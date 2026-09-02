n, m = map(int, input().split())

# Process robot A's movements
A = []
a_pos = 0
for _ in range(n):
    t, d = input().split()
    
    if d == 'R' : 
        sign = 1
    else: 
        sign = -1

    for _ in range(int(t)):
        a_pos += sign
        A.append(a_pos)


# Process robot B's movements
B = []
b_pos = 0
for _ in range(m):
    t, d = input().split()
    
    if d == 'R' : 
        sign = 1
    else: 
        sign = -1

    for _ in range(int(t)):
        b_pos += sign
        B.append(b_pos)

# Please write your code here.
cnt = 0

for i in range(1, max(len(A), len(B))):
    if i >= len(A):
        A.append(A[i-1])
    elif i >= len(B):
        B.append(B[i-1])
    
    if (A[i-1]!=B[i-1]) and (A[i]==B[i]):
        cnt += 1

print(cnt)