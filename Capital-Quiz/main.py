#
# Name Luke Guild
# Date 11/17/2024
# Capital Quiz Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Set a constant for number of states to test
NUM_STATES = 5
def main():
# Initialize the capitals 
    state_capitals = state_capitals_dictionary()
# Variables to keep count of correct and incorrect
    correct = 0
    incorrect = 0
# Start testing 
    for count in range(NUM_STATES):
# Get random entry
        state, capital = state_capitals.popitem()
# Ask user question
        print ('What is the capital of ', state, '? ',end='')
        response = input()
# See if they are correct
        if response.lower() == capital.lower():
            correct += 1
            print ('Correct')
        else:
            incorrect += 1
            print ('Incorrect')
# Show the results
    print ('Correct responses: ', correct)
    print ('Incorrect responses: ', incorrect)



import random

def state_capitals_dictionary():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South       Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    return capitals

# Call the main function.
main()
