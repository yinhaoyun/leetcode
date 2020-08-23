import json
from itertools import accumulate
from typing import List


# https://leetcode.com/problems/find-latest-group-of-size-m/
class Solution:

    # https://leetcode.com/problems/find-latest-group-of-size-m/discuss/806786/JavaC%2B%2BPython-Count-the-Length-of-Groups-O(N)
    def findLatestStep(self, arr, m):
        # print(f"findLatestStep: arr={arr}, m={m}")
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        # print(f"findLatestStep: length={length}, count={count}")
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            # print(f"iter {i}, a={a}, left={left}, right={right}")
            length[a] = length[a - left] = length[a + right] = left + right + 1
            # print(f"iter {i}, a={a}, length[{a}]={length[a]}, length[{a - left}]={length[a - left]}, length[{a + right}]={length[a + right]}")
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            # print(f"iter {i}, count={count}")
            if count[m]:
                res = i + 1
                # print(f"iter {i}, res={res}")
            # print()
        return res

    def another_stubid_idea(self, arr: List[int], m: int) -> int:
        n = len(arr)
        binary_list = [0] * n
        latest = -2
        for i, bit in enumerate(arr):
            binary_list[bit-1] = 1
            prefix_sum = list(accumulate(binary_list))
            for j, s in enumerate(prefix_sum):
                if s == m:
                    latest = i
        return latest + 1



    # TLE
    def use_string(self, arr: List[int], m: int) -> int:
        n = len(arr)
        found_bin = f"0{'1' * m}0"
        print(f"findLatestStep: n={n}, arr={arr}, m={m}, found_bin={found_bin}")
        integer, latest = 0, -2
        for i, bit in enumerate(arr):
            integer |= 1 << (bit-1)
            normalize_bin = "0" + bin(integer)[2:] + "0"
            # print(f"step {i+1}, {normalize_bin}")

            if found_bin in normalize_bin:
                print(f"found: step {i+1}, {normalize_bin}")
                latest = i
        return latest + 1 # from step 1


if __name__ == "__main__":
    s = Solution()
    with open("data/find_latest_group_of_size_m.json") as json_file:
        data = json.load(json_file)
        for d in data:
            result = s.findLatestStep(d['arr'], d['m'])
            print(f"result={result}, except={d['except']}")