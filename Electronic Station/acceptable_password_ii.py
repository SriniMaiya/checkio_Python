#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run acceptable-password-ii

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

# def is_acceptable_password(pwd: str) -> bool:
#     return len(pwd) >=6 and any([x.isdigit() for x in pwd]
def is_acceptable_password(pwd: str) -> bool:
    return len(pwd) >=6 and any(map(str.isdigit, pwd))

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")