#
# Name Luke Guild
# Date 11/11/2024
# Vowels and Consonants Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
def count_vowels(s):
# Define the vowels
    vowels = "aeiouAEIOU"
# Start the vowel count
    count = 0
# Go through the string and count vowels
    for char in s:
        if char in vowels:
            count += 1
    return count
def count_consonants(s):
# Define the consonants
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTUVWXYZ"
# Start the consonant count
    count = 0
# Go through the string and count consonants
    for char in s: 
        if char in consonants:
            count += 1
    return count
# Main program
def main():
# Ask user for a string
    user_input = input("Enter a string")
# Count vowels and consonants
    vowel_count = count_vowels(user_input)
    consonant_count = count_consonants(user_input)
# Display results
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}") 
# Run it
if __name__ == "__main__":
    main()

