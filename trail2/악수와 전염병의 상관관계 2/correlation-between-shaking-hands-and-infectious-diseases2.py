N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes.sort(key=lambda x: x[0])

# Please write your code here.
infection = {P:K}

for _, x, y in handshakes:
    if x in infection and y not in infection and infection[x]>0:
        infection[x] -= 1
        infection[y] = K
    elif y in infection and x not in infection and infection[y]>0:
        infection[y] -= 1
        infection[x] = K
    elif x in infection and y in infection:
        infection[x] -= 1
        infection[y] -= 1

        if infection[x] < 0:
            infection[x] = 0
        if infection[y] < 0:
            infection[y] = 0

# print(infection.keys())

for i in range(N):
    # print(i)
    if i+1 in infection.keys():
        print(1, end='')
    else:
        print(0, end='')


