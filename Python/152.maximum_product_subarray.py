from typing import List


# https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        dp1 = [0] * N
        dp2 = [0] * N
        dp1[0] = dp2[0] = nums[0]
        for i in range(1, N):
            if nums[i] >= 0:
                dp1[i] = max(nums[i], dp1[i-1] * nums[i])
                dp2[i] = min(nums[i], dp2[i-1] * nums[i])
            else:
                dp1[i] = max(nums[i], dp2[i-1] * nums[i])
                dp2[i] = min(nums[i], dp1[i-1] * nums[i])
        return max(dp1)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))  # 6
    print(s.maxProduct([-2,0,-1]))  # 0
    print(s.maxProduct([0, 2]))  # 2
    print(s.maxProduct([3,-1,4]))  # 4
