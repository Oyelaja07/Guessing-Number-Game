# secret_number = 7
# number_of_guesses = 0

# while number_of_guesses < 3:
#     guess = int(input("Guess the secret number: "))
#     number_of_guesses += 1

#     if guess == secret_number:
#         print("You won")
#         break
#     else:
#         print("Wrong guess")

# if guess != secret_number:
#     print("You lose")
secret_number = 7
number_of_guesses = 0
guess_limit = 3

while number_of_guesses < guess_limit:
    guess = input("Guess the secret number: ")

    if guess.isnumeric():
        guess = int(guess)
        number_of_guesses += 1

        if guess == secret_number:
            print("You won")
            break
        else:
            print("Wrong guess")
    else:
        print("Please enter numbers only")

if number_of_guesses == guess_limit and guess != secret_number:
    print("You lose")