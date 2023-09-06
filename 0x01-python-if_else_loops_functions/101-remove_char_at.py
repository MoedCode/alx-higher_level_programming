#!/usr/bin/python3
def remove_char_at(str, n):
    """creates a copy of the string, removing the character at the position n 
     (not the Python way, the “C array index”)."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
