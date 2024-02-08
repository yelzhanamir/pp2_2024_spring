from itertools import permutations
def print_permutations(string):
    vars= permutations(string)  
    for var in vars:
        print(var)  

input = input("Введите строку: ")
print("Все перестановки строки:")
print_permutations(input)
