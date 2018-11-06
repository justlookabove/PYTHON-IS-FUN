
secret_word = "giraffe"
guess = ""
guess_counter = 0
guess_limit = 5
guess_limit_reached = False


while guess != secret_word and not (guess_limit_reached):
    if guess_counter < guess_limit:
        guess = raw_input("Enter your guess: ")
        guess_counter += 1
    else:
        guess_limit_reached = True

if guess_limit_reached:
    print("YOU LOSE!")
else:
    print("YOU WIN!")