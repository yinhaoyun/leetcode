class Solution:
    def minOperations(self, n: int) -> int:
        mid = int(((n-1) / 2) * 2 + 1)
        return sum([mid - e for e in range(1, mid, 2)])


s = Solution()
print(s.minOperations(3))  # 2: [1, 3, 5]
print(s.minOperations(6))  # 9: [1, 3, 5, 7, 9, 11]