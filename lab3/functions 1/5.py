from itertools import permutations
def print_permutations(string):
    vars= permutations(string)  
    for var in vars:
        print(var)  

input = input("enter string: ")
print("all permutations:")
print_permutations(input)
