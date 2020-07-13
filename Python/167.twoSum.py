from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        find_num = target - numbers[0]
        while i < j:
            while numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            i += 1


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # 2
