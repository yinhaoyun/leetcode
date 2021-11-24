from typing import List


class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        i, j, ans = 0, 0, []
        while i < len(fl) and j < len(sl):
            start = max(fl[i][0], sl[j][0])
            end = min(fl[i][1], sl[j][1])
            if start <= end:
                ans.append([start, end])
            if fl[i][1] < sl[j][1]:
                i += 1
            else:
                j += 1
        return ans