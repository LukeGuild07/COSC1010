#
# Name Luke Guild
# Date 9/22/2024
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Initialize Variables
amount_spent = 0
# Ask user to enter amount budgeted
budget = int(input('What is your budget for the month?: '))
# Create variable to control loop
keep_going = 'y'
# Get expenses using a loop
while keep_going == 'y':
# Get amount spent on expense
    expense = int(input('Enter expense: '))
    amount_spent = expense + amount_spent
# See if user wants to enter another expense
    keep_going = input ('Do you have another expense? (Enter y for yes): ')
# Display amount over/under budget
if amount_spent <= budget:
    print('You were $',budget-amount_spent,'under your budget')
else:
    print('You were $',amount_spent-budget,'over your budget')