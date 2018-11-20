#In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".

# My solution

def dna_strand(dna):
    dicti = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join(dicti[x] for x in dna)
#dna_strand("ATTGC")

#Clever

def dna_strand1(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))
#dna_strand1("TAACG")

#NOTES ON maketrans()

translate_from = 'aeiou'
translate_to = '6510_'
sentence = 'I see you are getting the hang of it'
print(sentence.translate(str.maketrans(translate_from, translate_to)))

#for it to work, translate_from and translate_to must have the same length. 






