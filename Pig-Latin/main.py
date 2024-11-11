#
# Name Luke Guild
# Date 11/11/2024
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
def convert_to_pig_latin(word):
#Remove the first letter and add AY
    return word[1:] + word[0] + "ay"
def pig_latin_sentence(sentence):
# Divide the sentence into words
    words = sentence.split()
# Convert to Pig Latin
    pig_latin_words = [convert_to_pig_latin(word) for word in words]
# Put the sentence back together
    return ' '.join(pig_latin_words)
# Ask user for sentence
sentence = input("Enter a sentence: ")
# Convert and display sentence
print("Pig Latin: ", pig_latin_sentence(sentence))