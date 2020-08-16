import itertools
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int], collectios=None) -> bool:
        if len(arr) < 3:
            return False
        is_odd = [a % 2 for a in arr]
        prefix_sum = [0] + list(itertools.accumulate(is_odd))
        for i in range(3, len(prefix_sum)):
            if prefix_sum[i] - prefix_sum[i-3] == 3:
                return True
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.threeConsecutiveOdds([2,6]))  # False
    print(s.threeConsecutiveOdds([2,6,4,1]))  # False
    print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))  # True