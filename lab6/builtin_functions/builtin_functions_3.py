def palindrome(string):
    string1 = string.lower()
    if string1 == string1[::-1]:
        return " "
    else:
        return " not "

string = str(input("Write string: "))
print("String is" + palindrome(string) + "palindrome")
