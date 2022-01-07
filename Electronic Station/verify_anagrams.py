#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run verify-anagrams

# An anagram is a type of word play,    the result of rearranging the letters of a word or phrase to produce a new word or phrase,    using all the original letters exactly once.    Two words are anagrams to each other if we can get one from another by rearranging the letters.    Anagrams are case-insensitive and don't take account whitespaces.    For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not.
# 
# You are given two words or phrase. Try to verify are they anagrams or not.
# 
# Input:Two arguments as strings.
# 
# Output:Are they anagrams or not as boolean (True or False)
# 
# Precondition:0 < |first_word| < 100;
# 0 < |second_word| < 100;
# Words contain only ASCII latin letters and whitespaces.
# 
# 
# END_DESC

def verify_anagrams(a, b):
    # your code here
    a_count = sorted([i+str(a.lower().count(i)) for i in set(a.replace(" ", "").lower())])
    b_count = sorted([i+str(b.lower().count(i)) for i in set(b.replace(" ", "").lower())])

    return  a_count == b_count

# def verify_anagrams(a, b):
#     return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())



if __name__ == '__main__':
    print("Example:")
    print(verify_anagrams('Programming', 'Gram Ring Mop'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

x = "Programming"
{i: x.count(i) for i in x.replace(" ", '').lower()}
y = 'Gram Ring Mop'