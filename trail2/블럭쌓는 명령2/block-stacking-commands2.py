n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
blocks = [0]*n

for command in commands:
    s, e = command
    for i in range(s-1, e):
        blocks[i] += 1

print(max(blocks))