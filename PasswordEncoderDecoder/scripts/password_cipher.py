import os
import string
import random
from my_module import encode, decode
from my_module import guidelines, password

# Boolean variables used in script
valid_input = False
encoded = False
decoded = False
custom = False

# String variables used in script
user_password = ""
encoded_password = ""
decoded_password = ""
strength = ""
user_input = ""
encode_order = ""

# Integer variables used for encode/decode
custom_start_key = 0
custom_key_increment = 0
custom_key_multiplier = 0
encoding_count = 10

# Prints greeting
print("Hello, this is a Password Cipher.")

# Checks what user wants to do
while(not valid_input):
    choice = input("Would you like to encode or decode: ")         
    
    # Checks user input is valid and starts program based on input
    valid_input, encoded, decoded = guidelines.checks_input(choice)

# Asks user for password
if(encoded):
    passes_requirement = False
    print("Theres are the minimum password requiements: \n"
          "Must be more than 8 characters. \n"
          "Cannot have spaces. \n"
          "Cannot have 3 or more of the same character consecutively.")
    
    # Asks users for valid password
    while(not passes_requirement):
        user_password = input("Enter your password: ")
        passes_requirement = password.password_check(user_password)
        
    # Determines and returns the strength of the password
    strength = password.password_strength(user_password)
    
    # Asks user for which encoding they want
    print("Please choose if you want Single, Variable, "
                           "Custom, or Random Encoding. \n"
              "Type Single for Single, Variable for Variable, etc.\n"
              "Warning: Custom encoding will not be able to be decoded.")
    
    encoded_password = user_password
    
    # Asks user for what encoding they want as long as they want
    while((user_input != "N") or (encoding_count == 0)):
        user_input = input("Choose your encoding: ")
        
        # Checks for single encoding
        if(user_input == "Single"):
            encoded_password = encode.single_encode(encoded_password)
            encode_order = encode_order + "S"
            encoding_count = encoding_count - 1
            
        # Checks for variable encoding
        elif(user_input == "Variable"):
            encoded_password = encode.variable_encode(encoded_password)
            encode_order = encode_order + "V"       
            encoding_count = encoding_count - 1
            
        # Checks for random encoding
        elif(user_input == "Random"):
            encoded_password = encode.random_encode(encoded_password)
            encode_order = encode_order + "R"       
            encoding_count = encoding_count - 1
            
        # Checks if custom has been ran before and asks for inputs
        elif(not custom and user_input == "Custom"):
            # Receives inputs
            custom_start_key = int(input("Enter key: "))
            custom_key_increment = int(input("Enter key increment: "))
            custom_key_multiplier = int(input("Enter multiplier: "))
            
            # Encodes message and updates variables
            encoded_password = encode.custom_encode(encoded_password, 
                                                    custom_start_key, 
                                                    custom_key_increment, 
                                                    custom_key_multiplier)
            encode_order = encode_order + "C"
            custom = True
            encoding_count = encoding_count - 1
        
        # Runs custom again using previous user inputs
        elif(custom and user_input == "Custom"):
            # Encodes message and updates variables
            encoded_password = encode.custom_encode(encoded_password, 
                                                    custom_start_key, 
                                                    custom_key_increment, 
                                                    custom_key_multiplier)
            encode_order = encode_order + "C"
            encoding_count = encoding_count - 1
        
        # Tells user number of encodes and if they wish to continue
        print("You have", encoding_count, "encodes left.")
        user_input = input("Would you like to do encode again? Y/N?")
     
    # Prints final encoded password and order
    print("This is your encoded password:", encoded_password)
    print("This is your encode_order:", encode_order)
    
    # If custom encoding was used, prints out the inputs
    if(custom):
        print("This is your key:", custom_start_key)
        print("This is your key increment:", custom_key_increment)
        print("This is your multiplier:", custom_key_multiplier)

# Goes through the decode process
elif(decoded):
    # Asks for password and encode order to go back through
    decoded_password = input("Enter your encoded password: ")
    encode_order = input("Enter your encode order: ")
    
    # Checks if random was used and exits out if true
    if("R" in encode_order):
        print("Used random encode. Unable to return decoded password.")
    else:
        # Checks if custom encode was used and asks for the inputs
        if("C" in encode_order):
            custom_start_key = int(input("Enter key: "))
            custom_key_increment = int(input("Enter key increment: "))
            custom_key_multiplier = int(input("Enter multiplier: "))  
        
        # Going backwards through the encode order, decodes the password
        for char in encode_order[::-1]:
            # Checks which encoding was used and decodes appropriately
            if(char == "S"):
                decoded_password = decode.single_decode(decoded_password)
            elif(char == "V"):
                decoded_password = decode.variable_decode(decoded_password)
            elif(char == "C"):
                decoded_password = decode.custom_decode(decoded_password, 
                                                    custom_start_key, 
                                                    custom_key_increment, 
                                                    custom_key_multiplier)
        
        # Prints out the decoded message
        print("This is your decoded password:", decoded_password)
    