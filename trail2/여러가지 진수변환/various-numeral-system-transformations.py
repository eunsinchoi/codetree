N, B = map(int, input().split())

# Please write your code here.
remains = []

while True:
    if N < B:
        remains.append(N)
        break
    
    remains.append(N % B)
    N = N // B

for i in remains[::-1]:
    print(i, end="")