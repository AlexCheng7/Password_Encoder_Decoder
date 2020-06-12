import os
import string
import random

def single_decode(encoded_password):
    """ Goes through a basic decode
    
    Parameters
    ----------
    encoded_password: string
        String to decode
     
    Returns
    -------
    decoded : string
        Returns the decoded string
    """
    
    key = 200
    decoded = ''
    
    # Iterates through each character and decodes it
    for n in encoded_password:
        character = chr(ord(n) - key) 
        decoded = decoded + character
        
    return decoded
   
def variable_decode(encoded_password):
    """ Decodes the variable encoded string
    
    Parameters
    ----------
    encoded_password: string
        String to decode
     
    Returns
    -------
    decoded : string
        Returns the decoded string
    """
    
    key = 150
    key_increment = 3
    key = key + (len(encoded_password) * key_increment)

    decoded = ''

    # Iterates and decodes each character backwards and decreases the key
    for char in encoded_password[::-1]:
        key = key - key_increment
        decoded = decoded + chr(ord(char) - key)

    # Having decoded backwards, flips the message back around
    decoded = decoded[::-1]
    
    return decoded
 
def custom_decode(encoded_password, custom_key, 
                    custom_increment, custom_multiplier):
    """ Decodes the custom encoded string
    
    Parameters
    ----------
    encoded_password: string
        String to decode
    custom_key
        User input start key
    custom_increment
        User input key increment
    custom_multiplier
        User input key increment multiplier
     
    Returns
    -------
    custom_decoded : string
        Returns the decoded string
    """
    
    # Initalizes variables
    key = custom_key
    key_increment = custom_increment
    key = key + (len(encoded_password) * (key_increment * custom_multiplier))
    custom_decoded = ''
    
    # Iterates and decodes each character backwards and decreases the key
    for char in encoded_password[::-1]:
        # Key is decreased by increment multiplier
        key = key - (key_increment * custom_multiplier)
        custom_decoded = custom_decoded + chr(ord(char) - key)

    # Having decoded backwards, flips the message back around
    custom_decoded = custom_decoded[::-1]
    
    return custom_decoded
    