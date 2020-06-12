import os
import string

def checks_input(user_input):
    """ Checks if user inputted "encode" or "decode" after 
        removing punctuation and making lower case 
    
    Parameters
    ----------
    user_choice: string
        String to check
     
    Returns
    -------
    valid : boolean
        Returns if the input was valid
    encode : boolean
        Returns if it was encode
    decode : boolean
        Returns if it was decode
    """
    
    valid = True
    encode = False
    decode = False
    
    # Removes punctuation and makes lower case
    for punctuation in string.punctuation:
        user_input = user_input.replace(punctuation, "")
    user_input = user_input.lower()
    
    
    # Checks if input was encode or decode
    if(user_input == "encode"):
        encode = True
    elif (user_input == "decode"):
        decode = True
    else:
        print("Please input either encode or decode and try again.")
        valid = False
        
    return (valid, encode, decode)