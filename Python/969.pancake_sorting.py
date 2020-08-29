from typing import List


# https://leetcode.com/problems/pancake-sorting/
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        result = []
        for i in range(len(A) -1, -1, -1):
            if A[i] == (i+1):
                continue
            ai = A.index(i+1)
            if ai != 0:
                result.append(ai + 1)
                A = A[ai::-1] + A[ai+1:]
            result.append(i+1)
            A = A[i::-1] + A[i+1:]
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.pancakeSort(A = [3,2,4,1]))  # [4,2,4,3]
    print(s.pancakeSort(A = [1,2,3]))  # []