import random

answer = int(random.randrange(1, 10))


def start_game():
    # Welcome player
    print("--------------------------------\n"
          "Welcome to the Number Guessing Game\n"
          "--------------------------------\n")
    # guess takes the input and then prints the output
    # continuously prompt player for a guess
    # answer = int(random.randrange(1, 10)) use this for random number generator
    answer = int(4)
    # tries = 0

    # find out how to get the 'pick a number string to only appear once'.
    # guess = int(input("Pick a number between 1-10: "))
    while True:
        # tries += guess
        guess = int(input("Pick a number between 1-10: "))

        if guess > answer:
            print("It's lower")
        elif guess < answer:
            print("It's Higher")
        else:
            print("Got it")
            play_again = input("Would you like to play again [y]es/[n]o?")
            if play_again.lower() == 'y':
                print(guess)
            else:
                print()
                break

    # print('Got it')

            # print(tries)
        # elif guess == answer:
        #     print("Got it\n"
        #           "It took you, {} guesses\n".format(int(tries)))




    # tries += 1

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

