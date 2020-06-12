import string

def password_check(input_password):
    """ Checks if user password meets requirements 
    
    Parameters
    ----------
    input_password: string
        User password to check
     
    Returns
    -------
    passes_check : boolean
        Returns if the password meets the requirements
    """
    
    passes_check = True
    
    # Checks password length
    if(len(input_password) < 8):
        passes_check = False
        print("Too short, try again")
    
    # Checks if there are spaces in the password
    if(" " in input_password):
        passes_check = False
        print("Can't have spaces in password, try again")
        
    # Checks if there are duplicate sequences in password
    for char in input_password:
        multiple_dupes = char+char+char
        if(multiple_dupes in input_password):
            passes_check = False
            print("Can not have 3 or more of the same "
            "word consecutively, try again")
            break
            
    return passes_check

def password_strength(input_password):
    """ Checks how strong the user password is 
    
    Parameters
    ----------
    input_password: string
        User password to check
     
    Returns
    -------
    password_condition : string
        Returns how strong the password is
    """
    
    password_condition = ""
        
    # Parameter Checks
    upper = False
    lower = False
    digit = False
    symbol = False
    symbol_list = {"!","#","$","%","&","'","(",")","*","+",",",
                   "-",".","/",":",";","<","=",">","?","@","[",
                   "^","_","`","{","|","}","~","\""}
    length = len(input_password)
   
    
    # Loops through password to check parameters
    for char in input_password:
        # Checks if any uppercase
        if(not upper):
            upper = char.isupper()
            
        # Checks if any lowercase
        if(not lower):
            lower = char.islower()
            
        # Checks if any digits
        if(not digit):
            digit = char.isdigit()
            
        # Checks if any symbols
        if(not symbol):
            symbol = char in symbol_list
            
    # Checks weak condition
    if((length >= 8 and length < 10) and (not digit) and (not symbol)):
        print("Password is weak. Contains less than 10 characters, "
              "no numbers, and no symbols")
        password_condition = "Weak"
        
    # Checks strong condition:
    elif((length >= 12) and digit and upper and lower and symbol):
        print("Password is strong. Contains at least 15 "
              "characters, at least 1 number, at least 1 symbol "
              "and at least 1 upper and lower case.")
        password_condition = "Strong" 
        
    # Checks medium condition:
    elif((length >= 10) and digit and upper and lower):
        print("Password is medium. Contains at least 10 "
              "characters, at least 1 number, and at "
              "least 1 upper and lower case.")
        password_condition = "Medium"
        
    else:
        print("Cannot determine strength of password.")
        password_condition = "Unknown"
        
    return password_condition