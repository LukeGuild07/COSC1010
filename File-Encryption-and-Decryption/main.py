#
# Name Luke Guild
# Date 12/03/24
# File Encryption and Decryption Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Start Encryption Program
def encrypt_file(input_file, output_file, codes):
    try:
        with open(input_file, 'r') as infile:
            text = infile.read()
# Encrypt the text with code dictionary
        encrypted_text = ''.join([codes.get(char, char)for char in text])
        with open(output_file, 'w') as outfile:
            outfile.write(encrypted_text)
        print(f"Encryption is completed. Encrypted file saved as {output_file}")
    except FileNotFoundError: 
        print(f"The file {input_file} was not found")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
# Dictionary of the codes
codes = {
    'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'^', 'c':'3', 'D':'*', 
    'd':'2', 'E':'!', 'e':'4', 'F':'(', 'f':'5', 'G':'$', 'g':'6', 
    'H':')', 'h':'7', 'I':'-', 'i':'1', 'J':'+', 'j':'8', 'K':'=', 
    'k':'0', 'L':'[', 'l':']', 'M':'{', 'm':'}', 'N':';', 'n':':', 
    'O':'<', 'o':'>', 'P':',', 'p':'.', 'Q':'?', 'q':'/', 'R':'&', 
    'r':'5', 'S':'#', 's':'6', 'T':'!', 't':'7', 'U':'$', 'u':'8',  
    'V':'%', 'v':'9', 'W':'@', 'w':'0', 'X':'|', 'x':'<', 'Y':'^', 
    'y':'*', 'Z':'=', 'z':'+', ' ':' ', 
}
# Encrypt File
input_file = 'text.txt'
output_file = 'encrypted.txt'
encrypt_file(input_file, output_file, codes)


# Decryption Program
def decrypt_file(input_file, output_file, codes):
    try:
# Undo the code
        reverse_codes = {v: k for k, v in codes.items()}

        with open(input_file, 'r') as infile:
            encrypted_text = infile.read()
# Decrypt the text using reverse codes dictionary
        decrypted_text = ''.join([reverse_codes.get(char, char) for char in encrypted_text])
        with open(output_file, 'w') as outfile:
            outfile.write(decrypted_text)
        print(f"Decryption is completed. File saved as {output_file}")
        print("Decrypted content:")
        print(decrypted_text)
    except FileNotFoundError:
        print(f"The file {input_file} was not found")
    except Exception as e:
        print(f"An error has occured: {e}")
# Decrypt the file
input_file = 'encrypted.txt'
output_file = 'decrypted.txt'
decrypt_file(input_file, output_file, codes)