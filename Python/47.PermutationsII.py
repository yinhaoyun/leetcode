from typing import List, Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cnt = Counter(nums)

        def backtrack(d: int = 0):
            if d == len(nums):
                ans.append(list(formed))
                return

            for n, freq in cnt.items():
                if freq == 0: continue
                formed.append(n)
                cnt[n] = freq - 1
                backtrack(d + 1)
                cnt[n] = freq
                formed.pop()

        formed = []
        backtrack()
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))