import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = collections.defaultdict(lambda: 0)
        for n in nums:
            dic[n] += 1
            if dic[n] == 2:
                del dic[n]
        return dic.keys()


s = Solution()
print(s.singleNumber([1, 2, 1, 3, 2, 5]))  # [3,5]
