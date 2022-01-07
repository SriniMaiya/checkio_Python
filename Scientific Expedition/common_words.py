#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run common-words
def checkio(line1: str, line2: str) -> str:
    # your code here
    # line1 = line1.split(',')
    # line2 = line2.split(',')
    
    # return ','.join(sorted([x for x in line1 if x in line2]))
    return ','.join(sorted(set(line1.split(",")).intersection(set(line2.split(",")))))


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
