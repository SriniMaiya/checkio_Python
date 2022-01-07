#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run acceptable-password-iv
def is_acceptable_password(pwd:str) -> bool:
    # return True if 6<=len(pwd)<=9 and any(map(str.isdigit, pwd))  and any(map(str.isalpha, pwd)) else True if len(pwd)>9 and \
    #                                     ( any(map(str.isalpha, pwd)) or any(map(str.isdigit, pwd))) else False
    return len(pwd) > 9  or (len(pwd) > 6 and any(ch.isdigit() for ch in pwd) and not pwd.isdigit())  



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
    print("Coding complete? Click 'Check' to earn cool rewards!")
x = "This is a "
