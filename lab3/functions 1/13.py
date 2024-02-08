import random
def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20)
    num_guesses = 0

    while True:
        guess = int(input("Take a guess.\n"))
        num_guesses += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print("Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

guess_the_number()