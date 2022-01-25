# A generator of passwords for the undecided

# Importing the libraries
import random

# The lists of letters, numbers and special numbers
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
            "S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ["!","@","$","%","&","*","#"]


# Setting up the inputs to be scrambled for a stronger password
print("Hello there.\nWelcome to the Password Generator.\nPlease follow the instructions and you will receive one.\n")
letters = int(input("How many letters do you want in your password? "))
special = int(input("How many special characters do you want to add to your password? "))
numbers = int(input("How many numbers do you want to add to your password? "))

# Setting up the password to nothing and ready to receive
password_string = []

# Choosing the letters randomly according to letters input
for letter in range(letters):
    password_string += random.choice(alphabet)

# Choosing the special characters randomly according to special input
for char in range(special):
    password_string += random.choice(special_characters)

# Choosing the numbers randomly according to numbers input
for no in range(numbers):
    password_string += random.choice(nos)

# Asking whether to shuffle the password or not and printing it
answer = input("Do you want to shuffle your password? ").lower()
if answer == "yes" or answer == "y" or answer == "ye":
    random.shuffle(password_string)
    password = ''.join(password_string)
    print(f"Your new password is {password}.")
else:
    password = ''.join(password_string)
    print(f"Your new password is {password}.")

