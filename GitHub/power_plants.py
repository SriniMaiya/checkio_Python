#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run power-plants

# This mission is another version of the”Power Supply”mission     originated fromoduvan's idea.
# You have to properly place the given power plants and supply power to all the cities.
# 
# The intercity network and the range of each power plant are given as input values.A power plant can provide power to the city where it’s been placed and within its range.You have to return a dictionary, where the key is the city in which you’ll place the power plant and the value is its range.
# 
# NOTE:
# 
# You will always be given enough or more power-plants.So it isn't always necessary to return all power-plant placements.
# 
# Input:The intercity network represented as a set of connections, where each connection is a tuple of two nodes connected with each other.The range of each power plant, represented as a list of integers.
# 
# Output:A dictionary of placements, where each key is the city in which you’ll place the power plant and each value is the corresponding range.
# 
# Precondition:3 ≤ number of cities ≤ 501 ≤ number of power-plantsrange of power-plant ≥ 0
# 
# 
# 
# 
# END_DESC

from typing import Set, Tuple, List, Dict

def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:
    return {}


if __name__ == '__main__':
    assert power_plants({('A', 'B'), ('B', 'C')}, [1]) == {'B': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')}, [2]) == {'C': 2}
    assert power_plants({('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')}, [1, 1]) == {'B': 1, 'E': 1}
    assert power_plants({('A', 'B'), ('B', 'C'), ('A', 'D'), ('B', 'E')}, [1, 0]) == {'B': 1, 'D': 0}

    print('The local tests are done. Click on "Check" for more real tests.')