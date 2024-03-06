def counter(string):
    upper = 0
    lower = 0
    for i in string:
        if i >= 'A' and i <= 'Z':
            upper+=1
        elif i >= 'a' and i <= 'z':
            lower+=1
    return [upper, lower]

string = str(input("Write string: "))
print("Number of uppercase letters: " + str(counter(string)[0]) + "\nNumber of lowercase letters: " + str(counter(string)[1]))
