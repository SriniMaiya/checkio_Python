#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run acceptable-password-vi

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit, but it cannot consist of just digits;having numbers or containing just numbers does not apply to the password longer than 9.a string should not contain the word "password" in any case;should contain 3 different letters (or digits) even if it is longer than 10Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

def is_acceptable_password(pwd: str) -> bool:
    c1 = len(pwd) >6 and (any([ch.isdigit() for ch in pwd]) and not pwd.isdigit())
    c2 = len(pwd) >9
    c3 = "password" not in pwd.lower()
    c4 = len(set(pwd))  >= 3

    return (c1 or c2) and c3 and c4



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")