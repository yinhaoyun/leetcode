from typing import List


# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(itvl_1: List[int], itvl_2: List[int]) -> bool:
            if itvl_1[0] > itvl_2[1] or itvl_1[1] < itvl_2[0]:
                return False
            return True
        ans = []
        for i in intervals:
            if overlap(i, newInterval):
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
            else:
                ans += [i]
        ans += [newInterval]
        ans.sort()
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))  # [[1,5],[6,9]]
    print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))  # [[1,2],[3,10],[12,16]]
