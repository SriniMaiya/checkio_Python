from itertools import zip_longest

def check_horizontals(text, word):
    """
    Search the word in the text by rows
    
    Args:
        text -- A list of strings
        word -- our "hidden" word
        
    Return:
        The row and column of the first letter of the word
    """
    for i, line in enumerate(text):
        if word in line:
            return i, line.index(word)
    return None, None


def checkio(text, word):
    """
    Search the "hidden" word in the text.
    
    Args:
        text -- Multiline string for search
        word -- our "hidden" word
        
    Return:
        The list with coordinates of the word
    """
    
    #normalize text in the matrix
    text = text.replace(" ", "").lower()
    data = text.split("\n")
    
    
    row, col = check_horizontals(data, word)
    if row is not None:
        return [row + 1, col + 1, row + 1, col + len(word)]
    
    #transpose text. zip_longest does not truncate rows.
    data = ("".join(row) for row in zip_longest(*data, fillvalue=""))
    
    row, col = check_horizontals(data, word)
    if row is not None:
        return [col + 1, row + 1, col + len(word), row + 1]
    
    raise ValueError("The rhyme does not contain the word.")


from time import time

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    s = time()
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
e = time()
print(e-s)
