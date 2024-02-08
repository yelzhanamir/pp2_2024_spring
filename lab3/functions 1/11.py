def is_palindrome(word):
    return word == word[::-1]

user_input = input("enter word: ")
if is_palindrome(user_input):
    print("YES")
else:
    print("NO")
