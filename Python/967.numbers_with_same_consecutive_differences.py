from typing import List


# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
class Solution:
    def __init__(self):
        self.numsSameConsecDiff = self.back_track_int
    def back_track_int(self, N: int, K: int) -> List[int]:
        if not N:
            return []

        result = []
        def helper(index: int, cur: int, formed: int) -> None:
            formed = formed * 10 + cur
            if index == N - 1:
                result.append(formed)
                return
            if cur - K >= 0:
                helper(index + 1, cur - K, formed)
            if K and cur + K < 10:
                helper(index + 1, cur + K, formed)
            return

        for i in range(0 if N == 1 else 1, 10):
            helper(0, i, 0)
        return result
    # 40 ms, 75.81%
    def back_track_list(self, N: int, K: int) -> List[int]:
        if not N:
            return []

        result = []
        formed = [0] * N

        def helper(index: int, cur: int) -> None:
            formed[index] = cur
            if index == N - 1:
                result.append(int(''.join([str(f) for f in formed])))
                return
            if cur - K >= 0:
                helper(index + 1, cur - K)
            if K and cur + K < 10:
                helper(index + 1, cur + K)
            return

        for i in range(0 if N == 1 else 1, 10):
            helper(0, i)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.numsSameConsecDiff(N = 0, K = 7))  # []
    print(s.numsSameConsecDiff(N = 3, K = 7))  # [181,292,707,818,929]
    print(s.numsSameConsecDiff(N = 2, K = 1))  # [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    print(s.numsSameConsecDiff(1, 0))
    print(s.numsSameConsecDiff(2, 0))