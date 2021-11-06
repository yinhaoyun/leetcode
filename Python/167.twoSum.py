from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return l + 1, r + 1
            elif target < s:
                r -= 1
            else:
                l += 1

    def twoSum_bsearch(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)

        def bsearch(left, right, tgt) -> int:
            nonlocal numbers, N

            while left <= right:
                mid = (left + right) >> 1
                if numbers[mid] == tgt:
                    return mid
                elif tgt < numbers[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        for i in range(N):
            j = bin_search(i + 1, N - 1, target - numbers[i])
            if j > 0:
                return [i + 1, j + 1]