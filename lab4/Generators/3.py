n = int(input("Enter n:"))
def test():
    for i in range(n+1):
        yield i + 1
a = test()
even_numbers = ", ".join(str(i) for i in a if i % 3 == 0 and i % 4 == 0 )
print(even_numbers)
