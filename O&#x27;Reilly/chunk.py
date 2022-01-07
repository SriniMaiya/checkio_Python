#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run chunk
from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    # your code here
    #return [items[n:n+size] for n in range(0, (len(items)//size)*size, size)] + [items[(len(items)//size)*size:]] if len(items)%size !=0 else [items[n:n+size] for n in range(0, (len(items)//size)*size, size)]
    return [items[i:i+size] for i in range(0, len(items), size)]


if __name__ == '__main__':
    print("Example:")
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("Coding complete? Click 'Check' to earn cool rewards!")
