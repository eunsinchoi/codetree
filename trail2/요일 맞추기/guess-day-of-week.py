m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
date = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
date_idx = 1

# 1월 1일부터 날짜 계산해서 구하기
def cal_days(m, d):
    days = 0
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(m):
        days += month_days[i]
    days += d
    return days


new_date_idx = int(
    (cal_days(m2, d2)-cal_days(m1, d1)+1)%7
)

print(date[new_date_idx])

# # 하루씩 시뮬레이션
# if m1 != m2:
#     sign = (m2-m1)/abs(m2-m1)
# else:
#     sign = (d2-d1)/abs(d2-d1)

# while True:
#     if m1==m2 and d1==d2:
#         break

#     date_idx += 1*sign
#     d1 += 1*sign

#     if d1 > month_days[m1]:
#         m1+=1
#         d1=1
    
#     if d1 < 1:
#         m1 -= 1
#         d1 = month_days[m1]


# new_idx = int(date_idx%7)
# print(date[new_idx])