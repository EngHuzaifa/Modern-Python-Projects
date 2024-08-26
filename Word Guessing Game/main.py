
import random ,pprint 

def word_guessing_game():

    # choose a word randomly from a list
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry','apple','mango']
    word = random.choice(words)
    
    # initialize variables
    guessed_letters = set()
    attempts = 6
    correct_guesses = 0
   
    
    print("Welcome to the Word Guessing Game! 🥰")

    print("<----------------------------------->")

    print('Guess a letter in the following word:')

    pprint.pprint(words)
   
    
   
    while attempts > 0:
       
        
        # get user input
        guess = input('Enter a letter: ').lower()
        
        # check if the guess is correct
        if guess in word:
            correct_guesses += word.count(guess)
            print(f'Correct! The letter "{guess}" appears {word.count(guess)} times.')


            # ask the user  do you want to play again? press 'y' to continue
            play_again = input('Do you want to play again? (y/n): ').lower()
            if play_again!= 'y':
             print('Thanks for playing! 😃')
             print("Goodbye! 😜")
             break
            
        else:
            attempts -= 1
            print(f'Incorrect! You have {attempts} attempts left.')
        
        # check if the player has won
        if correct_guesses == len(word):
            print('Congratulations! You have guessed the word correctly.')
        
        # check if the player has lost
        if attempts == 0:
            print(f'Sorry, you have run out of attempts. The word was "{word}".')
            

        
word_guessing_game()

    
                




