#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run isometric-strings

# Maybe it's a cipher? Maybe, but we don’t know for sure.
# 
# Maybe you can call it"homomorphism"? I wish I knew this word before.
# 
# You need to check that the 2 given strings are isometric. This means that a character from one string can become a match for characters from another string.
# 
# One character from one string can correspond only to one character from another string. Two or more characters of one string can correspond to one character of another string, but not vice versa.
# 
# Input:Two arguments. Both strings.
# 
# Output:Boolean.
# 
# Precondition:
# both strings are the same length
# 
# 
# END_DESC

def isometric_strings(a, b):
    # your code here
    return len(set(zip(a,b))) == len(set(a))


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))
    print(isometric_strings("googpy", "doodle"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")