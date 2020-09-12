from typing import List


# https://leetcode.com/problems/combination-sum-iii/
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(formed: List[int]) -> None:
            if len(formed) == k and sum(formed) == n:
                ans.append(formed)
                return
            for i in range(formed[-1] + 1, 10):
                dfs(formed + [i])
        for i in range(1, 10):
            dfs([i])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 7))  # [[1,2,4]]
    print(s.combinationSum3(3, 9))  # [[1,2,6], [1,3,5], [2,3,4]]