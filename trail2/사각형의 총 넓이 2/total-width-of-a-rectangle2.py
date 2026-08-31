n = int(input())
positions = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for xi in range(x1, x2):
        for yi in range(y1, y2):
            positions.append((xi, yi))

print(len(set(positions)))