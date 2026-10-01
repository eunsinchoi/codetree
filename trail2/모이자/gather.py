n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_dist = float('inf')
dist = 0
for i in range(n):
    for j in range(n):
        dist += abs(i-j)*A[j]
    min_dist = min(min_dist, dist)
    dist = 0


print(min_dist)