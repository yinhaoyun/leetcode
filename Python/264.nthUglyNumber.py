class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]
        i2 = i3 = i5 = 0  # index
        while len(ugly_nums) != n:
            next_ugly = min(ugly_nums[i2] * 2, ugly_nums[i3] * 3, ugly_nums[i5] * 5)
            if next_ugly == ugly_nums[i2] * 2:
                i2 += 1
            if next_ugly == ugly_nums[i3] * 3:
                i3 += 1
            if next_ugly == ugly_nums[i5] * 5:
                i5 += 1
            ugly_nums.append(next_ugly)
            print(ugly_nums, i2, i3, i5)
        return ugly_nums[n-1]

s = Solution()
print(s.nthUglyNumber(n = 10))  # 12