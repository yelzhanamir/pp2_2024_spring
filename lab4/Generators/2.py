n = int(input("Enter n:"))
def test():
    for i in range(n):
        yield i + 1
a = test()
even_numbers = ", ".join(str(i) for i in a if i % 2 == 0)
print(even_numbers)
