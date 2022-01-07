#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run sort-except-zero
from typing import Iterable


def except_zero(items: list) -> Iterable:
    # your code here    print(s)
    # non_z = sorted([x for x in items if x])
    # i = 0
    # for ind, item in enumerate(items):
    #     if item != 0:
    #         items[ind] = non_z[i]
    #         i += 1
    #         if i == len(non_z):
    #             return items

    # return items
    it = iter(sorted(e for e in items if e))
    yield from [next(it) if e else 0 for e in items]

if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")

x = ('1','2','3')
' '.join(x)