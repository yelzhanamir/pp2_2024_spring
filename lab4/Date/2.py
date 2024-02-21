import datetime

x = datetime.datetime.now()

print("yesterday's date:", x.day-1, x.month, x.year)
print("today's date:", x.day, x.month, x.year)
print("tomorrow's date:", x.day+1, x.month, x.year)