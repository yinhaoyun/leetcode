from typing import List


class Solution:

    # Lexicographic (Binary Sorted)
    def subsets_bitmask(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        N_BIT = 1 << N
        ans = []
        for i in range(2**N):
            bitmask = bin(i | N_BIT)[3:]
            ans += [[nums[i] for i, b in enumerate(bitmask) if b == "1"]]

        return ans

    def subsets_cascading(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            ans += [a + [n] for a in ans]
        return ans


    def subsets_backtrack(self, nums: List[int]) -> List[List[int]]:
        ans = []
        formed = []

        def backtrack(cur = 0):
            ans.append(list(formed))
            if len(formed) == len(nums):
                return
            for i in range(cur, len(nums)):
                formed.append(nums[cur])
                backtrack(i + 1)
                formed.pop()

        backtrack()
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(comb: List[int], n: int):
            if n == len(nums):
                # print(comb)
                res.append(list(comb))
                return

            # pick
            comb.append(nums[n])
            helper(comb, n+1)
            comb.pop()
            helper(comb, n+1)
            # not pick

        helper([], 0)
        return res



s = Solution()
print(s.subsets(nums = [1,2,3]))
print(s.subsets_backtrack(nums = [1,2,3]))
print(s.subsets_cascading(nums = [1,2,3]))
print(s.subsets_bitmask(nums = [1,2,3]))