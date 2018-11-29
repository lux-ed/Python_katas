def order(sentence):
    splitted = sentence.split()

    result = []

    for word in splitted:
        for letter in word:
            if letter.isdigit():
                result.append([int(letter), word]) #appends it as a list, first the integer then the word itself
    return " ".join(x[1] for x in sorted(result))
order("is2 Thi1s T4est 3a")


