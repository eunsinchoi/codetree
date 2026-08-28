N = input()

# Please write your code here.
def ten_to_two(n):
    remains = []
    num_2 = str()

    while True:
        if n < 2:
            remains.append(n)
            break
        
        remains.append(n%2)
        n = n//2

    for i in remains[::-1]:
        num_2 += str(i)
    
    return num_2


def two_to_ten(num_2):
    num_10 = 0

    for i in num_2:
        num_10 = num_10*2 + int(i)
        

    return num_10

result = ten_to_two(two_to_ten(str(N))*17)
print(result)