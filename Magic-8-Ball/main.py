#
# Name Luke Guild
# Date 11/2/24
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Get the randomizer
import random
# Open file
def load_response(file_name):
    with open(file_name,'r') as file:
        responses = [line.strip() for line in file.readlines()]
    return responses
# Ask user question
def magic_8_ball():
    responses = load_response('8_ball_responses.txt')

    print("This is the Magic 8 Ball")
    while True:
        question = input("Ask a YES or NO question (or type 'q' to quit): ")
        if question.lower() == 'q':
            print ("When you need me come ask")
            break
        if question.strip() == "":
            print ("Please ask a question")
            continue
# Randomly select the response
        response = random.choice(responses)
        print(f"The Magic 8 Ball says: {response}")

if __name__ == "__main__":
    magic_8_ball()