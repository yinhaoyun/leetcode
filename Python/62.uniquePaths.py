class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [1] * m
        # print(arr)
        for y in range(1, n):
            for x in range(1, m):
                arr[x] += arr[x - 1]
            # print(arr)
        return arr[m - 1]


s = Solution()
print(s.uniquePaths(m=3, n=2))
print(s.uniquePaths(m=7, n=3))
