#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run unix-match-part-1
def unix_match(filename: str, pattern: str) -> bool:
    if '*' in pattern:
        
        return pattern[pattern.find('*'):] in filename
    return len(pattern) == len(filename) 
        
    # your code here
    return filename == pattern

if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
