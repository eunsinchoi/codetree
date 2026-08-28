n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
line = [0]*200

for seg in segments:
    start, end = seg[0]+100, seg[1]+100
    for i in range(start, end):
        line[i] += 1
    
print(max(line))
