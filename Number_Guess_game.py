# Number Guessing Game using while loop

secret_number = 25

while True:
    guess = int(input("Guess the secret number: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break
    