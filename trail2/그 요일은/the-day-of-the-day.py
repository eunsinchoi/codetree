m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
week_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def cal_days(m, d):
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    
    for i in range(m):
        days += month_days[i]
    days += d

    return days

diff_days = cal_days(m2, d2)-cal_days(m1, d1)
# print(f"diff_days : {diff_days}")
index_of_a = week_day.index(A)
# print(f"index_of_a : {index_of_a}")

if A=='Mon':
    count = 1
else:
    count = 0
    
for i in range(1, diff_days+1):
    if i%7 == index_of_a:
        count += 1

print(count)