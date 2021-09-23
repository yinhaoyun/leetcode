from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        formed = []
        nums.sort()

        def backtrack(d: int = 0) -> None:
            ans.append(list(formed))
            for i in range(d, len(nums)):
                if i != d and nums[i] == nums[i - 1]:
                    continue
                formed.append(nums[i])
                backtrack(i + 1)
                formed.pop()

        backtrack()
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1,2,2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(s.subsetsWithDup([0])) # [[],[0]]
