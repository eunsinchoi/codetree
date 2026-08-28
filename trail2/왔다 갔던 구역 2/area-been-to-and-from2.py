n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
pos = 0
passed = {}


for step in range(n):
    if dir[step]=='R':
        for i in range(x[step]):
            if pos + i not in passed:
                passed[pos + i] = 1
            else:
                passed[pos + i] += 1
        pos += x[step]
    elif dir[step] == 'L':
        for j in range(pos - x[step], pos):
            if j not in passed:
                passed[j] = 1
            else:
                passed[j] += 1

        pos -= x[step]

count = 0
for key, value in passed.items():
    if value >= 2:
        count += 1

print(count)