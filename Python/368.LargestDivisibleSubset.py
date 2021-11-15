class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [(-1, 1)]  # (prev_idx, length),
        for i, n in enumerate(nums[1:]):
            max_idx = -1
            for j, d in enumerate(dp):
                if n % nums[j] == 0:
                    if max_idx < 0 or dp[max_idx][1] < d[1]:
                        max_idx = j
            dp.append((max_idx, dp[max_idx][1] + 1 if max_idx >= 0 else 1))
        max_idx = -1
        for i, d in enumerate(dp):
            if max_idx < 0 or d[1] > dp[max_idx][1]:
                max_idx = i
        ans = [-1] * dp[max_idx][1]
        for i in range(len(ans) - 1, -1, -1):
            ans[i] = nums[max_idx]
            max_idx = dp[max_idx][0]
        return ans
