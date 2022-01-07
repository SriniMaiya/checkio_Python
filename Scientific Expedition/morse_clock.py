#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run morse-clock
def checkio(time_string: str) -> str:
    mapper = {x: bin(int(x))[2:].zfill(4).replace('0','.').replace('1','-') for x in "0123456789"}
    time_string = time_string.split(":")
    time = [" ".join([mapper[d] for d in x.zfill(2)])[1:] for x in time_string]
    
    #replace this for solution
    return " : ".join(time)[1:]

if __name__ == '__main__':
    print("Example:")
    print(checkio("10:37:49"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    print("Coding complete? Click 'Check' to earn cool rewards!")

