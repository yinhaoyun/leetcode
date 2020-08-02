from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        :param arr: 3 <= arr.length <= 100
                0 <= arr[i] <= 1000
        :param a, b, c:
                0 <= a, b, c <= 1000
        """
        ret = 0
        n = len(arr)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, n):
                    if abs(arr[j] - arr[k]) <= b and \
                            abs(arr[i ] - arr[k]) <= c:
                        ret += 1
        return ret


s = Solution()
print(s.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))  # 4
print(s.countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))  # 0