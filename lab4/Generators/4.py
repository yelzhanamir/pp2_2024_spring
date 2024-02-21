a=int(input("Enter a "))
b=int(input("Enter a "))
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

for square in squares(a, b):
    print(square)