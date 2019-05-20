import random
import pyfiglet


def start_game():
    # welcome player
    name = input("Hello please enter your name to start the game (or 'quit' to quit): ")
    if name == 'quit':
        quit()
    else:
        welcome = pyfiglet.figlet_format("welcome!! {}".format(name.title()), font='cyberlarge')
        saw = pyfiglet.figlet_format("Lets Play a Number Guessing Game")
        print(welcome)
        print(saw)

    atmpts = 0
    answer = random.randint(0, 9)
    while True:
        atmpts += 1
        try:
            guess = int(input("Pick a number between 1-10: "))

            if guess == answer:
                print("You did it!!")
                print("It took you {} attempts".format(atmpts))
                game_replay = input("Would you like to play again [y]es/[n]o?")

                if game_replay == 'y':
                    atmpts = 0
                    continue

                else:
                    print("You did great. See you later.")
                    break

            elif guess > answer:
                print("It's lower")
            elif guess < answer:
                print("It's Higher")
        except ValueError:
            # err does not give the item that caused the err
            print("Please enter a number between 1-10.")
        else:
            continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
