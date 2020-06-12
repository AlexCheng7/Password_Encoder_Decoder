import os
import string
import random

def single_encode(input_password):
    """ Goes through a basic encode
    
    Parameters
    ----------
    input_password: string
        String to encode
     
    Returns
    -------
    encoded : string
        Returns the encoded string
    """
    
    key = 200
    encoded = ''
    
    # Iterates through each character and encodes it
    for n in input_password:
        character = chr(ord(n) + key) 
        encoded = encoded + character
        
    return encoded

def variable_encode(input_password):
    """ Variable encodes the string
    
    Parameters
    ----------
    input_password: string
        String to encode
     
    Returns
    -------
    encoded : string
        Returns the encoded string
    """
    
    key = 150
    key_increment = 3
    encoded = ''
    
    # Iterates and encodes each character and increases the key
    for n in input_password:
        character = chr(ord(n) + key) 
        encoded = encoded + character
        key = key + key_increment
        
    return encoded


def custom_encode(input_password, custom_key, 
                    custom_increment, custom_multiplier):
    """ Variable custom encodes the string
    
    Parameters
    ----------
    input_password: string
        String to encode
    custom_key
        User input start key
    custom_increment
        User input key increment
    custom_multiplier
        User input key increment multiplier
     
    Returns
    -------
    custom_encoded : string
        Returns the encoded string
    """
    
    # Initalizes variables
    key = custom_key
    key_increment = custom_increment
    custom_encoded = ''
    
    # Iterates and encodes each character and increases key
    for n in input_password:
        character = chr(ord(n) + key) 
        custom_encoded = custom_encoded + character
        # Key is increased by increment multiplier
        key = key + (key_increment * custom_multiplier)
        
    return custom_encoded       
        
def random_encode(input_password):
    """ Randomly encodes the string
    
    Parameters
    ----------
    input_password: string
        String to encode
     
    Returns
    -------
    encoded : string
        Returns the encoded string
    """
    
    # Sets key to random start
    key = random.randint(0, 400)
    key_increment = 0
    encoded = ''
    
    # Each iteration randomizes key and increment
    for n in input_password:
        character = chr(ord(n) + key)
        encoded = encoded + character
        
        # Randomizes the values
        key_increment = random.randint(0, 15)
        key = random.randint(0, 400)
        
        key = key + key_increment
        
    return encoded
        