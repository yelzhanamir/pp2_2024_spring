from datetime import datetime


date1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")


date2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")


difference = abs(date2 - date1)


difference_sec = difference.total_seconds()

print("Difference between the two dates in seconds:", difference_sec)
