#
# Name Luke Guild
# Date 9/29/2024
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.
# Setup Function
def feet_to_inches(feet):
# Convert Feet To Inches
    return feet * 12
def main():
# Ask user for feet
    feet = float(input("Enter number of feet"))
    inches = feet_to_inches(feet)
# Display feet compared to inches
    print(f"{feet} feet is equal to {inches} inches")
if __name__ == "__main__":
    main()
