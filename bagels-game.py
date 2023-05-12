import random

print("This was inspired by Al Sweigart's 'The Big Book of Small Python Projects'. To view the code that inspired "
      "this alternate version of Al's project, please visit https://inventwithpython.com/bigbookpython/project1.html "
      "\n")

NUM_GUESSES = 10
NUM_DIGITS = 3


def main():
    print(f"Guess the {NUM_DIGITS}-digit number. The order the clues are delivered in will be shuffled, so where the "
          f"clue is does not reflect which digit of your guess the clue refers to. Clues:\n"
          f"Right on:   right number, right position\n"
          f"Close:      right number, wrong position\n"
          f"Nope:       wrong number, wrong position\n")

    playing = True
    while playing:
        secret_number = get_secret_num()
        print(f"The secret number has been chosen!")
        attempt = 1

        while attempt <= NUM_GUESSES:
            print(f"Attempt #{attempt}:\n")
            guess = input("> ")

            if len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Please guess a number with {NUM_DIGITS} digits.")
                continue

            clues = get_clues(guess, secret_number)
            print(clues)

            if guess == secret_number:
                break

            attempt += 1

            if attempt > NUM_GUESSES:
                print(f"Sorry, you ran out of tries. The secret number was {secret_number}.")

        ask_to_play = True
        while ask_to_play:
            play_again = input("Do you want to play again? (y/n).\n").lower()
            if play_again.startswith("n"):
                input("Thanks for playing!\n"
                      "Press enter to exit the game.")
                playing = False
                break
            elif play_again.startswith("y"):
                break
            else:
                print("Please type either 'y' or 'n'.")


def get_secret_num():
    secret_number = ""
    for num in range(1, NUM_DIGITS+1):
        digit = str(random.randint(0, 9))
        secret_number += digit

    return secret_number


def get_clues(guessed_number, actual_number):
    clues = []

    if guessed_number == actual_number:
        return "You got it!"

    # prepare actual_number for replacing digits with None
    actual_number = list(actual_number)

    for i in range(len(guessed_number)):
        if guessed_number[i] == actual_number[i]:
            clues.append("Right on")
            actual_number[i] = None
        elif guessed_number[i] in actual_number:
            clues.append("Close")
            # to replace only the first instance of actual_number that guessed_number[i] matches:
            guessed_digit = guessed_number[i]
            for j in range(len(actual_number)):
                if actual_number[j] == guessed_digit:
                    actual_number[j] = None
                    break
        else:
            clues.append("Nope")

        # Replacing guessed digits with None solves problem of "If digit in guessed_number is only in actual_number
        # once, but guessed_number includes that digit twice, they get told twice that it"s a correct guess,
        # leading to the incorrect impression that the digit really is in actual_number twice" by removing digit from
        # answer after both types of successful guess.

    random.shuffle(clues)
    return "", "".join(clues)


if __name__ == "__main__":
    main()
