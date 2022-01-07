#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run most-wanted-letter

# You are given a text, which contains different English letters and punctuation symbols.    You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,    "A" == "a".    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# 
# If you havetwo or more letters with the same frequency,    then return the letter which comes first in the Latin alphabet.    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# 
# Input:A text for analysis as a string.
# 
# Output:The most frequent letter in lower case as a string.
# 
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105
# 
# 
# END_DESC

def checkio(text: str) -> str:
    text = ''.join(x.lower() for x in text if x.isalpha())

    dic = {}
    for l in text:
        if l not in dic.keys():
            dic[l] = 1
        else: dic[l] += 1
    return (sorted(dic.items(), key = lambda x: (-x[1], x[0]))[0][0])

 
  

if __name__ == '__main__':
    print("Example:")
    print(checkio("AAAooo!!!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")