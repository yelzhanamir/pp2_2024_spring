def solve(numheads, numlegs):
    numchickens= (4*numheads-numlegs)/2
    numrabbits= numheads-numchickens
    if type(numchickens)==int and type(numrabbits)==int:
        print("numchickens=",numchickens)
        print("numrabbits=",numrabbits)
    else:
        print("it is impossible")

    
numlegs=int(input("Enter numlegs: "))
numheads=int(input("Enter numheads: "))

solve(numheads, numlegs)
