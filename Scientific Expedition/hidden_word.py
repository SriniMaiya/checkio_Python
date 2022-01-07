#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run hidden-word
def checkio(text, word):
    text = text.replace(" ","").split("\n")
    try:
        for ind, line in enumerate(text):
            if word in line:
                return [ind+1, x:=line.find(word)+1,ind+1, x+len(word)-1]

    except Exception as e:
        print(e)

    try:
        for i in range(0,len(text)-len(word)+1):
            for j in range(min([len(text[i]) for i in range(i,i+len(word))])):

                cmp = "".join([text[k][j] for k in range(i,i+len(word))]).lower()
                print(cmp)
                if cmp == word:
                    print([i+1, x:=j+1, i+len(word), x ])
                    return [i+1, x:=j+1, i+len(word), x ]
    except Exception as e:
        print(e)

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

