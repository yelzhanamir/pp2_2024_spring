n=int(input("Enter n "))
def countdown(n):
    while n >= 0:
        yield n
        n -= 1



for number in countdown(n):
    print(number)
