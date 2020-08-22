from bisect import bisect
from itertools import accumulate
from random import randrange
from random import random
from typing import List


# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        weights = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        self.weights = [w / sum(weights) for w in accumulate(weights)]

    # Runtime: 208 ms, faster than 76.02%
    def pick(self) -> List[int]:
        rect_index = bisect(self.weights, random())
        x1, y1, x2, y2 = self.rects[rect_index]
        x, y = randrange(x1, x2 + 1), randrange(y1, y2 + 1)
        return [x, y]

    # Runtime: 316 ms, faster than 14.03%
    def my_binary_search(self) -> List[int]:
        pick_rand = randrange(self.weights[-1])
        # print(f"pick_rand={pick_rand}, weights={self.weights}")
        start_i, end_i = 0, len(self.weights)
        while True:
            rect_index = start_i + ((end_i - start_i - 1) // 2)
            # print(f"bi_search rect_index={rect_index}, start_i={start_i}, end_i={end_i}")
            # print(f"cur_range={self.weights[rect_index]}~{self.weights[rect_index+1]}")
            if self.weights[rect_index] <= pick_rand < self.weights[rect_index + 1]:
                break
            if pick_rand < self.weights[rect_index]:
                end_i = rect_index
            else:
                start_i = rect_index + 1

        x1, y1, x2, y2 = self.rects[rect_index]
        x, y = randrange(x1, x2 + 1), randrange(y1, y2 + 1)
        return [x, y]


def exec_case(rects: List[List[int]]) -> None:
    s = Solution(rects)
    for _ in range(5):
        print(s.pick())


if __name__ == '__main__':
    exec_case([[1, 1, 5, 5]])
    exec_case([[-2, -2, -1, -1], [1, 0, 3, 0]])
    exec_case([[82918473, -57180867, 82918476, -57180863], [83793579, 18088559, 83793580, 18088560], [66574245, 26243152, 66574246, 26243153], [72983930, 11921716, 72983934, 11921720]])
    exec_case([[-2, -2, -1, -1], [1, 0, 3, 0], [100, 200, 105, 205]])
    exec_case([[-58953616, -40483558, -58953446, -40482555], [76369640, 94978791, 76371036, 94979394], [80970826, -37466957, 80971657, -37466388], [-79821573, -4177978, -79820536, -4177925]])

