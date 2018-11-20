# You must find that single number that is different from the rest.

def stray(num):
    for i in num:
        if num.count(i) == 1:
            return i


