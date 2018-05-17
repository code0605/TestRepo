
def get_indices(word,char):
    indices = []
    for index,letter in enumerate(word):
        if letter == char:
            indices.append(index)
    return indices



print(get_indices("banana","a") == [1,3,5])
