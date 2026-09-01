n, m = map(int, input().split())


def positions(n):
    A = []
    pos = 0
    for _ in range(n):
        direction, time = input().split()
        if direction == 'R':
            sign = 1
        elif direction == 'L':
            sign = -1
        for _ in range(int(time)):
            pos = pos+sign
            A.append(pos)
    return A

# Please write your code here.
a = positions(n)
b = positions(m)

i=0
while i < min(len(a), len(b)):
    if a[i] == b[i]:
        print(i+1)
        break
    else:
        i+=1
else:
    print(-1)