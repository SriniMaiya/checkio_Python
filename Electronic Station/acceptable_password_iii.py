#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run acceptable-password-iii
def is_acceptable_password(pwd:str) -> bool:
    return True if len(pwd)>=6 and any(map(str.isdigit, pwd))  and any(map(str.isalpha, pwd)) else False

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
x = "12asafde"
