#!/home/srini/.checkio/checkio_chrome_plugin.py --domain=py run similar-triangles
from typing import List, Tuple
Coords = List[Tuple[int, int]]
from math import sqrt

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    
    s11 = sqrt((coords_1[1][0] - coords_1[0][0])**2 + (coords_1[1][1] - coords_1[0][1])**2)
    s12 = sqrt((coords_1[2][0] - coords_1[1][0])**2 + (coords_1[2][1] - coords_1[1][1])**2)
    
    s21 = sqrt((coords_2[1][0] - coords_2[0][0])**2 + (coords_2[1][1] - coords_2[0][1])**2)
    s22 = sqrt((coords_2[2][0] - coords_2[1][0])**2 + (coords_2[2][1] - coords_2[1][1])**2)
    # your code here
    print(s11,s12, s21, s22)
    return s11/s21 == s12/s22 or s11/s22 == s12/s21


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")

