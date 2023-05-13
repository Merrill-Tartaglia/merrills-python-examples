import random

print("This was inspired by Al Sweigart's 'The Big Book of Small Python Projects'. \n"
      "To view the code that inspired this alternate version of Al's project, please visit \n"
      "https://inventwithpython.com/bigbookpython/project10.html \n")

print("Welcome to Cho-han, or the even-odd game! We're going to roll a couple dice and you're going to bet on whether "
      "the number the rolls add up to is even or odd. \n"
      "For every correct bet, the house takes a percentage from the player's winnings.\n")

while True:
    players_num = input("How many players would you like? (1-4)\n> ")
    if not players_num.isdecimal():
        print("Please type a number.\n")
    elif int(players_num) < 1 or int(players_num) > 4:
        print("Please type 1, 2, 3, or 4.\n")
    else:
        players_num = int(players_num)
        break

names_all = []
players_dict = {}
for person in range(1, players_num + 1):
    name = input(f"What is player {person}'s name?\n> ").title()
    names_all.append(name)
    players_dict[name] = [5000, "bet placeholder", "prediction placeholder"]

print()

names_fake = []
# There must be more than 1 player to ask about computer players.
if players_num > 1:
    while True:
        players_fake_num = input(f"How many artificial players would you like? (0-{players_num - 1})\n> ")
        if not players_fake_num.isdecimal():
            print("Please type a number.\n")
        elif int(players_fake_num) < 0 or int(players_fake_num) > (int(players_num) - 1):
            print("Please type a valid number.\n")
        else:
            players_fake_num = int(players_fake_num)
            break

    for a_name in range(players_fake_num):
        while True:
            comp_name = input("What is the name of the player who isn't real?\n> ").title()
            if comp_name not in names_all:
                print(f"Name not recognized. Your players are named:")
                for p_name in names_all:
                    print(p_name)
                print()
            else:
                names_fake.append(comp_name)
                break

        print()

names_real = []
for name in names_all:
    # if computer players exist, determine who is a human player before adding their name. Otherwise, just add their
    # name.
    try:
        if name not in names_fake:
            names_real.append(name)
    except NameError:
        names_real.append(name)

playing = True
while playing:

    print("Purse amounts:")
    for person, values in players_dict.items():
        purse_amt = players_dict[person][0]
        print(f"{person}: {purse_amt}")

    print()

    if len(names_fake) > 0:
        for person_fake in names_fake:
            purse_num = players_dict[person_fake][0]
            try:
                comp_bet = random.randrange((round(purse_num * .25)), purse_num, (round(purse_num * .25)))
            except ValueError:
                comp_bet = purse_num
            players_dict[person_fake][1] = comp_bet
            print(f"{person_fake} bets {comp_bet}.")

            comp_predict = random.choice(["even", "odd"])
            players_dict[person_fake][2] = comp_predict
            print(f"{person_fake} predicts that the roll will be {comp_predict}.\n")
            input("To continue, press enter.\n")

    for person_real in names_real:
        while True:
            bet = input(f"{person_real}, what amount do you want to bet?\n> ")
            if not bet.isdecimal():
                print("Please type a number.\n")
            elif int(bet) > players_dict[person_real][0]:
                print("You cannot bet more than you have. Please bet lower.\n")
            else:
                bet = int(bet)
                players_dict[person_real][1] = bet
                print()
                break

        while True:
            prediction = input(f"{person_real}, will the sum of the two dice rolls be even or odd? (e/o)\n> ").lower()
            if prediction.startswith("e"):
                print("'Even' selected.\n")
                prediction = "even"
                break
            elif prediction.startswith("o"):
                print("'Odd' selected.\n")
                prediction = "odd"
                break
            else:
                print("Please type either 'even' or 'e', or else type 'odd' or 'o'.\n")

        players_dict[person_real][2] = prediction

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"The first die rolled a {dice1}!\nThe second die rolled a {dice2}!\nThe number is {dice1 + dice2}.\n")

    rolled_even = (dice1 + dice2) % 2 == 0

    for name in names_all:
        if rolled_even and players_dict[name][2] == "even":
            correct = True
        elif rolled_even and players_dict[name][2] == "odd":
            correct = False
        elif not rolled_even and players_dict[name][2] == "even":
            correct = False
        elif not rolled_even and players_dict[name][2] == "odd":
            correct = True

        amount_of_bet = players_dict[name][1]
        # players_dict[name][0] edits purse amount
        if correct:
            print(f"{name}, you won your bet!")
            house_fee = amount_of_bet // 10
            amt_gained = amount_of_bet - house_fee
            print(f"The house takes {house_fee} as a fee. Purse increased by {amt_gained}!")
            players_dict[name][0] += amt_gained
            input("Press enter to continue.\n")

        else:
            print(f"Sorry {name}, you lost {amount_of_bet}.")
            players_dict[name][0] -= amount_of_bet
            input("Press enter to continue.\n")

        if players_dict[name][0] < 1:
            print(f"Tough luck, {name}! You've run out of money!\n")

    for key in list(players_dict.keys()):
        if players_dict[key][0] < 1:
            if key in names_fake:
                names_fake.remove(key)
            if key in names_real:
                names_real.remove(key)
            names_all.remove(key)
            del players_dict[key]

    if players_num > 1 and len(names_all) == 0:
        print("Oops, no one has any money left!\n")
        playing = False
    elif players_num == 1 and len(names_all) == 0:
        playing = False
    else:
        while True:
            want_to_play = input("Do you want to keep playing? (y/n)\n> ").lower()
            if want_to_play.startswith("n"):
                print()
                playing = False
                break
            elif want_to_play.startswith('y'):
                break
            else:
                print("Please enter 'yes' or 'y', or else enter 'no' or 'n'.\n")

input("Thanks for playing!\n"
      "Press enter to exit.")
