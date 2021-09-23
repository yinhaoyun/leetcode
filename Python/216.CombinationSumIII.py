from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr: int, remain: int) -> None:
            if remain == 0 and len(formed) == k:
                ans.append(list(formed))
                return

            for i in range(curr, 10):
                if remain - i < 0:
                    break
                formed.append(i)
                backtrack(i + 1, remain - i)
                formed.pop()
        ans = []
        formed = []
        backtrack(1, remain = n)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(k = 3, n = 7)) # [[1,2,4]]
    print(s.combinationSum3(k = 3, n = 9)) # [[1,2,6],[1,3,5],[2,3,4]]
    print(s.combinationSum3(k = 4, n = 1)) # []
    print(s.combinationSum3(k = 3, n = 2)) # []
    print(s.combinationSum3(k = 9, n = 45)) # [[1,2,3,4,5,6,7,8,9]]