days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = int(input())

month = 1

while n > days_in_month[month - 1]:
    n -= days_in_month[month - 1]
    month += 1 

print(n, month)
