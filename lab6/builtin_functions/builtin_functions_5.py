def true_values(tuple):
    for i in tuple:
        if not i:
            return False
    return True

tuple = (1, "Hello", 1.234, True, 'a', ["s"])
print(true_values(tuple))
