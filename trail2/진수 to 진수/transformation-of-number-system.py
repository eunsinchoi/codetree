a, b = map(int, input().split())
n = input()

# Please write your code here.
# A to 10
num = 0
for i in str(n):
    num = num*a + int(i)

# 10 to B
remains = []
while True:
    if num < b:
        remains.append(num)
        break
    
    remains.append(num%b)
    num = num // b

for i in remains[::-1]:
    print(i, end='')

