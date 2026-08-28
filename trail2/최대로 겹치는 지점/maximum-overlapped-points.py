n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
line = [0]*101

for segment in segments:
    x1, x2 = segment
    for i in range(x1, x2+1):
        line[i] += 1

print(max(line))