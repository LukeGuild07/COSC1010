#
# Name Luke Guild
# Date 10/20/2024
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Open he file
with open('number.txt','r') as file:
# Examine each line
    for line in file:
# Get rid of whitespace and display
        print(line.strip())