def multiply(list):
    result = 1
    for i in list:
        result*=i
    return result
    
string = (str(input("Write list: ")).strip()).split(" ")
list = [int(i.strip()) for i in string]
print(multiply(list))
