import random ,pprint

print('Welcome to the Hangman Game! 🥰') 
print('<------------------------------------->')

print('Rules: ��')
print('1. The game will randomly select a word from a predefined list.')
print('2. You have a limited number of attempts to guess the word.')
print('3. Each incorrect guess will deduct one attempt.')
print('4. If you run out of attempts, the word will be revealed to you.')
print('5. Good luck! ��') 
print('<------------------------------------->')

print('Guess the word! HINT: word is a name of a programming languages')

def hangman():
    words:list[str] = ['python', 'java', 'ruby', 'javascript', 'c++', 'swift', 'C#']
    pprint.pprint(words)

    word:str = random.choice(words)
    guessed_letters = set()
    max_attempts:int = 10
    attempts_left = max_attempts

    while attempts_left > 0:
        print(f"Attempts left: {attempts_left}")
        print("Guessed letters:", ', '.join(sorted(guessed_letters)))
        print("Current word:", ''.join(['_' if letter not in guessed_letters else letter for letter in word]))

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts_left -= 1
            print("Incorrect guess. Try again.")

            continue
        
        if '_' not in ''.join(['_' if letter not in guessed_letters else letter for letter in word]):
            print("Congratulations! You've guessed the word:", word)

            break

hangman()
