"""
Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) 
represented as a string. The value is typically broken into 5 sections in an 
8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'

Algorithm:
1. Generate string of random ascii_letters + digits followed by a dash
2. Pop the last dash
"""

import random

characters = 'abcdef01234567789'
uuid_sequence = [8, 4, 4, 4, 12]

def generate_uuid():
    uuid = ''
    for length in uuid_sequence:
        uuid += ''.join(random.choice(characters) for _ in range(length)) # use the _ when the actual value isn't important 
        uuid += '-'        
    return uuid[:-1]

generate_uuid()