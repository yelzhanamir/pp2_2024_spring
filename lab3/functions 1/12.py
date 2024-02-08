def histogram(numbers):
    for num in numbers:
        print('*' * num)

d = input("Enter Histogram: ")
numbers = [int(num) for num in d.split()]
histogram(numbers)