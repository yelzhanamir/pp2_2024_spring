def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)
