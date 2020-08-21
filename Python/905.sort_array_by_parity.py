from typing import List


# https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    def __init__(self):
        self.sortArrayByParity = self.onelinear

    # 72 ms, faster than 99.01%
    def double_ptr(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while True:
            while A[i] % 2 == 0 and i < j:
                i += 1
            while A[j] % 2 == 1 and i < j:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
            else:
                break
        return A

    def onelinear(self, A: List[int]) -> List[int]:
        return [a for a in A if a % 2 == 0] + [a for a in A if a % 2 == 1]


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([3,1,2,4]))
    print(s.sortArrayByParity([1,2,3,4]))
    print(s.sortArrayByParity([1,3,5, 7]))
    print(s.sortArrayByParity([2,4,6, 8]))
    print(s.sortArrayByParity([]))
