# Function to XOR each character with 13
def xor_with_13(input_string):
    #String  initialized to ""
    new = ""

    for char in input_string:

        # Convert the character to  integer counterpart
        char_value = ord(char)

        # XOR with 13
        xor_13 = char_value ^ 13

        # Convert the XOR result back to a character
        new += chr(xor_13)

    return new

# Original string
string = "label"

# XOR the string with 13
xored_string = xor_with_13(string)

# Construct the flag
flag = f"crypto{{{xored_string}}}"

# Print the flag
print(flag)
