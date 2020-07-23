import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for n in nums:
            diff ^= n
        diff &= -diff

        ret = [0, 0]
        for n in nums:
            if n & diff:
                ret[0] ^= n
            else:
                ret[1] ^= n
        return ret


s = Solution()
print(s.singleNumber([1, 2, 1, 3, 2, 5]))  # [3,5]
