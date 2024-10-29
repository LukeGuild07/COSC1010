#
# Name Luke Guild
# Date 10/28/2024
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Import The Random
import random
def generate_lottery_number():
# Generate The List
    lottery_number = [random.randint(0,9) for _ in range (7)]
    return lottery_number
def display_lottery_number(lottery_number):
# Display The List
    print ("Your lottery number is:")
    for digit in lottery_number:
        print (digit, end='')
# Use a Newline For Better Formattng
    print()
# Generate and Display
lottery_number = generate_lottery_number()
display_lottery_number(lottery_number)
