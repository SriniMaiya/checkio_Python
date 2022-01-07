#!/home/srini/anaconda3/envs/tfgpu/bin/checkio --domain=py run follow-instructions

# You’ve received a letter from a friend whom you haven't seen or heard from for a while. In this letter he gives you instructions on how to find a hidden treasure.
# 
# In this mission you should follow a given list of instructions which will get you to a certain point on the map. A list of instructions is a string, each letter of this string points you in the direction of your next step.
# 
# The letter "f" - tells you to move forward, "b" - backward, "l" - left, and "r" - right.
# 
# It means that if the list of your instructions is "fflff" then you should move forward two times, make one step to the left and then again move two times forward.
# 
# Now, let's imagine that you are in the position (0,0). If you move forward your position will change to (0, 1). If you move again it will be (0, 2). If your next step is to the left then your position will become (-1, 2). After the next two steps forward your coordinates will be (-1, 4)
# 
# Your goal is to find your final coordinates. Like in our case they are (-1, 4)
# 
# Input:A string.
# 
# Output:A tuple (or list) of two ints
# 
# Precondition:only chars f,b,l and r are allowed
# 
# 
# END_DESC

from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
    # your code here
    # ins = {"f":[0,1],"b":[0,-1],"l":[-1,0],"r":[1,0]}
    # val = [ins[x] for x in instructions]

    # return tuple(sum(y) for y in zip(*val))
    spawn = (0,0)
    c = instructions.count
    return spawn[0] + c("r") - c("l"), spawn[1] + c("f") - c("b")

follow = lambda i: [i.count(x)-i.count(y) for x, y in ('rl', 'fb')]

if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")