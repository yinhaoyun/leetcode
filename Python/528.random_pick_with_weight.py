from bisect import bisect
from itertools import accumulate
from random import randrange
from typing import List


# https://leetcode.com/problems/random-pick-with-weight/
class Solution:

    def __init__(self, w: List[int]):
        self.weights = list(accumulate(w))

    # Runtime: 212 ms, faster than 95.36%
    def pickIndex(self) -> int:
        return bisect(self.weights, randrange(self.weights[-1]))


def exec_case(w: List[int]) -> None:
    s = Solution(w)
    for _ in range(5):
        print(s.pickIndex())


if __name__ == '__main__':
    exec_case([1])
    exec_case([1,3])
