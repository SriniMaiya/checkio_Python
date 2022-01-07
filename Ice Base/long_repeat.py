#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run long-repeat
from itertools import groupby
# def long_repeat(line: str) -> int:
#     """
#         length the longest substring that consists of the same char
#     """
#     # your code here
#     line = ["".join(group) for key, group in groupby(line)]
#     print(line)
#     return max([len(x) for x in line]) if line else 0

def long_repeat(line: str) -> int:
    return max(len(list(g)) for _,g in groupby(line)) if line else 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')


