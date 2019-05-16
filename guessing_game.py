import random


def start_game():
    # Welcome player
    print("--------------------------------\n"
          "Welcome to the Number Guessing Game\n"
          "--------------------------------\n")
    # Variables for while loop
    games_plated = 0
    atmpts = 0
    answer = int(random.randrange(1, 10))
    # continuously prompt player for a guess
    while True:
        guess = int(input("Pick a number between 1-10: "))
        games_plated += 1
        atmpts += 1
        if guess > answer:
            print("It's lower")
        elif guess < answer:
            print("It's Higher")
        else:
            print("Got it")
            print("It took you {} atempts".format(atmpts))
            play_again = input("Would you like to play again [y]es/[n]o?")
            if play_again.lower() == 'y':
                continue
            else:
                print("The game has ended, You played {} times and it took you {} attempts.\n"
                      "See you later next time".format(games_plated, atmpts))
                break


    # """Psuedo-code Hints
    #
    # When the program starts, we want to:
    # ------------------------------------
    # 1. Display an intro/welcome message to the player.
    # 2. Store a random number as the answer/solution.
    # 3. Continuously prompt the player for a guess.
    #   a. If the guess greater than the solution, display to the player "It's lower".
    #   b. If the guess is less than the solution, display to the player "It's higher".
    #
    # 4. Once the guess is correct, stop looping, inform the user they "Got it"
    #      and show how many attempts it took them to get the correct number.
    # 5. Let the player know the game is ending, or something that indicates the game is over.
    #
    # ( You can add more features/enhancements if you'd like to. )
    # """
    # # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

