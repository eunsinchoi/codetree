n = int(input())

# Please write your code here.
remains=[]

if n==0:
    remains=[0]

while n != 0:
    remains.append(n%2)
    n = n//2

for remain in remains[::-1]:
    print(remain, end="")
    