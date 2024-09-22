#
# Name Luke Guild
# Date 9/22/2024
# Bug Collector Programming Project
# COSC 2409 DNT
#
# Initialize variables for bugs and total number of bugs collected.
total_bugs=0
# Get number of bugs collected each day using a for loop.
for day in range(1, 6):
    print('Enter the number of bugs collected on day', day)
    bugs= int(input())
    total_bugs= total_bugs+ bugs
# Display the total number of bugs collected.
print('You have collected a total of',total_bugs,'bugs')