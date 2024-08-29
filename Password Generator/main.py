import random
import string

def generate_password(length=6):
   
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    password = [random.choice(lowercase_letters), random.choice(uppercase_letters), random.choice(digits), random.choice(special_characters)]
    
    # Fill the rest of the password length with random characters from all sets
    for _ in range(length - 4):
        password.append(random.choice(all_characters))
    
    # Shuffle the characters to make the password more secure
    random.shuffle(password)
    
    # Convert the list of characters back into a string
    return ''.join(password)


password = generate_password()
print("Generated Password:", password)

# write the password is strong
if len(password) >=6 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(char in string.punctuation for char in password):
        print("The password is strong")
else:
        print("The password is weak")



generate_password()





