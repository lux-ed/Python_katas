#Write a function that will convert a string into title case, given an optional list of exceptions (minor words).
# The list of minor words will be given as a string with each word separated by a space.
#  Your function should ignore the case of the minor words string -- 
# it should behave in the same way even if the case of the minor word string is changed.

def title_case(title, minor_words = ''):
    return ' '. join(word if word in minor_words.lower().split() else word.title() for word in title.capitalize().split())
    

#def title_case(title, minor_words = 'None'): WORKS TOO. 