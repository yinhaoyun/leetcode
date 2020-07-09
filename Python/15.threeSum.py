from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # print(nums)
        for i in range(len(nums)-2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j, k = i+1, len(nums) - 1
            # print("i=", i)
            while j < k:
                x = -nums[i]
                y = nums[j] + nums[k]
                # print("i=", i, "j=", j, "x=", x, "y=", y)
                if y < x:  #
                    j += 1
                elif y > x:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]: j+=1;
                    while j < k and nums[k] == nums[k - 1]: k-=1
                    j, k = j+1, k-1

        return res
        

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4],))  # [  [-1, 0, 1],  [-1, -1, 2] ]
print(s.threeSum([0,0,0,0]))  # [[0,0,0]]