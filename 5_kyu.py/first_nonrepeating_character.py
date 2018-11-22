#Function takes a string input and returns the first character that is not 
#repeated anywhere in the string. Upper and lowercase letters are considered
#the same character. If the string contains all repeating characters, it should
#return empty string. 

def first_non_repeating_char(string):
    for c in string:
        if string.lower().count(c.lower()) == 1:
            return c
    return ''



