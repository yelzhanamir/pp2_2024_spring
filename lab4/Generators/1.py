n=int(input("Enter n:"))
def test():
    for i in range(n+1):
        yield i*i
a=test()

for i in test():
    print(i)