number = 10
print("I'm thinking of a number...")
guesses_left = 3
while True:
    guess = input(f"What number am I thinking of? (You have {guesses_left} guesses left. Enter 'q' to quit) ")
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guesses_left -= 1
        if guesses_left == 0:
            print(f"Sorry! You have no more guesses left. The number was {number}.")
            break
        else:
            print(f"Sorry! That's not the right number. You have {guesses_left} guesses left.")
