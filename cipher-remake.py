try:
    import pyperclip
except ImportError:
    pass

print("This was inspired by Al Sweigart's 'The Big Book of Small Python Projects'. \n"
      "To view the code that inspired this alternate version of Al's project, please visit \n"
      "https://inventwithpython.com/bigbookpython/project6.html \n")

symbols = "abcdefghijklmnopqrstuvwxyz:.\",'!?() 0123456789"

playing = True
while playing:
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)?\n> ").lower()
        if mode.startswith("e"):
            mode = "encrypt"
            break
        elif mode.startswith("d"):
            mode = "decrypt"
            break
        else:
            print("Please type either an e or a d.")

    # max_shift_num calculation chosen randomly, I just wanted user to be able to choose a number larger than the length
    # of symbols, but not large enough to slow the program down too much.
    max_shift_num = round(len(symbols) * 3.6)
    while True:
        shift_num = input(f"How many places do you want to shift by? (0-{max_shift_num})\n> ")
        if shift_num.isdecimal() and int(shift_num) <= max_shift_num:
            shift_num = int(shift_num)
            break
        else:
            print(f"Please type a number between 0 and {max_shift_num}.")

    message_in = input(f"What message would you like to {mode}?\n> ").lower()
    message_out = ""
    for symbol in message_in:
        if symbol in symbols:
            symbol_index = symbols.find(symbol)

            if mode == "encrypt":
                symbol_index += shift_num
            elif mode == "decrypt":
                symbol_index -= shift_num

            while True:
                if symbol_index >= len(symbols):
                    symbol_index -= len(symbols)
                elif symbol_index < 0:
                    symbol_index += len(symbols)

                try:
                    symbol = symbols[symbol_index]
                    break
                except IndexError:
                    # Allows user to input a shift_num larger than length of symbols
                    continue
        message_out += symbol

    print(f"Your message is:\n{message_out}")

    try:
        pyperclip.copy(message_out)
        print("Your message has been copied.")
    except ImportError:
        pass

    play_again = input("Would you like to go again? (y/n)\n> ").lower()
    if play_again.startswith("y"):
        continue
    else:
        input("Goodbye!\n"
              "Press enter to exit.")
        playing = False

