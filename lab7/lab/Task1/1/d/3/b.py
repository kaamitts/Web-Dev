from datetime import date, timedelta

day, month, year = map(int, input().split())

current_date = date(year, month, day)

future_date = current_date + timedelta(days=2)

print(future_date.day, future_date.month, future_date.year)
