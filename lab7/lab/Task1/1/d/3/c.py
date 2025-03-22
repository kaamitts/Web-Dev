def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date = input().strip()
d = int(date[:2])   
m = int(date[2:4])  
y = int(date[4:])   

days_count = 0
for year in range(1, y): 
    days_count += 366 if is_leap(year) else 365

for month in range(1, m):
    days_count += days_in_month[month - 1]
    if month == 2 and is_leap(y):
        days_count += 1

days_count += d

print(days_count)
