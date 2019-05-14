import random

# play_again = input("Would you like to play again [y]es/[n]o?")
# answer = int(input(random.randrange(1, 10)))


def start_game():
    # Welcome player
    print("--------------------------------\n"
          "Welcome to the Number Guessing Game\n"
          "--------------------------------\n")
    # guess takes the input and then prints the output
    guess = int(input("Pick a number between 1-10: "))

    # while not answer:
    #     tries = 0
    #     if guess > answer:
    #         print("It's lower")
    #     if guess < answer:
    #         print("It's Higher")
    #     if guess == answer:
    #         print("Got it\n"
    #               "It took you, {} guesses\n".format(int(tries)))
    #         print(play_again)
    #         if play_again.upper() == 'y':
    #             continue
    #         else:
    #             break
    #
    #     tries += 1

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

