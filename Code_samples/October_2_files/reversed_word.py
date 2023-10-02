# a program that reverses a word - prints it out backwards

ANIMALS = ["iguana","elephant","retriever","terrapin","cat","finch", "Great Dane"]

def reverse_word(animal):   #parameter is the word to be reversed
    reversed_word = []
    for letter in range(len(animal)-1,-1,-1):
        reversed_word.append(animal[letter])
    reversed_string = ''.join(reversed_word)
    return reversed_string

def multi_reverse_word(wildlife):  # wildlife is going to be the list of  animal names
    new_animals = []
    for critter in wildlife:
        new_animals.append(reverse_word(critter))

    return new_animals

if __name__ == "__main__":


    """
    for critter in ANIMALS:

#    word = "iguana"
       backwards = reverse_word(critter)
       print(critter, "backwards is ", backwards)
"""
    new_wildlife_list = multi_reverse_word(ANIMALS)
    print(new_wildlife_list)