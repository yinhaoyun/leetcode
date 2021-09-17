from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i1, i2 = 0, 0
        ans = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                ans.append(nums1[i1])
                i1, i2 = i1+1, i2+1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return ans



if __name__ == "__main__":
    s = Solution();
    print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2])) # [2,2]
    print(s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])) # [4,9]