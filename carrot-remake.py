import random

print("This was inspired by Al Sweigart's 'The Big Book of Small Python Projects'. \n"
      "To view the code that inspired this alternate version of Al's project, please visit \n"
      "https://inventwithpython.com/bigbookpython/project9.html \n")

playing = True
while playing:
    print("Welcome to the carrot game! Let's pretend every player has a box. One of your boxes contains a carrot. "
          "Try to end up with that carrot in your box at the end of the game!\n")

    while True:
        num_of_players = input("How many people are playing?\n> ")
        if not num_of_players.isdecimal():
            print("Please enter a number.")
            continue
        else:
            num_of_players = int(num_of_players)
            break

    player_dict = dict()
    for player_num in range(1, num_of_players + 1):
        player_dict[player_num] = input(f"What is player {player_num}'s name?\n> ")

    who_has_carrot_now = player_dict[random.randint(1, num_of_players)]

    for player in range(1, num_of_players):
        next_player = player + 1
        input(
            f"Everyone who isn't {player_dict[player]} or who hasn't already seen their box, close your eyes. "
            f"Then press enter to reveal contents of {player_dict[player]}'s box.\n> ")

        if who_has_carrot_now == player_dict[player]:
            print(f"{player_dict[player]}, you have a box with a carrot in it!")
        else:
            print(f"{player_dict[player]}, you've never had a carrot in your life. Your box is empty.")

        input("When you're ready to move on, press enter.\n> ")
        print('\n' * 100)

        print(
            f"{player_dict[player]}, please tell other player(s) to open their eyes, and tell them whether you "
            f"have the carrot. Feel free to lie.\n")

        switch = input(f"{player_dict[next_player]}, do you want to swap boxes with {player_dict[player]}? "
                       f"(y/n)\n> ").lower()

        if switch.startswith("y"):
            if who_has_carrot_now == player_dict[player]:
                who_has_carrot_now = player_dict[next_player]
            elif who_has_carrot_now == player_dict[next_player]:
                who_has_carrot_now = player_dict[player]

    input("When ready, press enter to find out the winner.\n> ")

    print(f"{who_has_carrot_now} is the winner!")

    while True:
        still_playing = input("Would you like to play again? (y/n)\n> ").lower()
        if still_playing.startswith("y"):
            print()
            break
        elif still_playing.startswith("n"):
            input("Thanks for playing!\n"
                  "Press enter to exit.")
            playing = False
            break
        else:
            print("Please type an answer containing either a y or an n.\n")
            continue
