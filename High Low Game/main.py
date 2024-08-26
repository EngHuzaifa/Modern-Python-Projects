import random

def high_low_score():

    print("Welcome to the High Low Game")

    print("<------------------------------->")

    score = 0

    while True:
        number = random.randint(1, 100)
        guess = int(input("Guess a number between 1 and 100: "))
        
        if guess == number:

            print("Congratulations! You guessed the correct number.")
            score += 1
            print(f"Your current score: {score}")

            play_again = input("Do you want to play again? (Y/N): ").lower()

            if play_again != 'y':
                print("Thanks for playing")
                break

        elif guess < number:

            print("Too low! Try again.")

        else:
            print("Too high! Try again.")

high_low_score()
   
