#
# Name Luke Guild
# Date 10/20/2024
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Initaliaze variables
total = 0
count = 0
# Open the file
with open('numbers.txt', 'r') as file:
# Read the lines in the file
    for line in file:
# Change line into an integer and add it to the total
        number = int(line.strip())
        total += number
        count += 1
# Figure out average
if count > 0:
    average = total/count
    print(f"The average of the numbers in the file is: {average}")
else:
    print("There are no numbers in the file.")