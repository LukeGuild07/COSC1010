#
# Name Luke Guild
# Date 10/28/2024
# Exception Handling Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
def calculate_average (filename):
    try:
        with open(filename,'r') as file:
            numbers = file.readlines()
# Convert Lines to Integers
        integers = []
        for num in numbers:
            try:
                stripped_num = num.strip()
# Check For Non-Empty Line
                if stripped_num:
                    integers.append(int(stripped_num))
            except ValueError:
                print(f"The line '{num.strip()}'is not a valid integer")
        if not integers:
            raise ZeroDivisionError ("No valid numbers")
    except IOError as io_error:
        print(f"An I/O arror occured")
    except ZeroDivisionError as e:
        print(f"{e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
# Call The Function With the Filename
calculate_average('numbers.txt')