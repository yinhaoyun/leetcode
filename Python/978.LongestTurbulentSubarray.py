from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 1
        anchor = 0

        def cmp(x, y) -> int:
            if x == y:
                return 0
            return 1 if x > y else -1
        for i in range(1, N):
            c = cmp(arr[i-1], arr[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * cmp(arr[i], arr[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i

        return ans



if __name__ == "__main__":
    s = Solution()
    print(s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9])) # 5
    print(s.maxTurbulenceSize([4,8,12,16])) # 2
    print(s.maxTurbulenceSize([100])) # 1
    print(s.maxTurbulenceSize([9,9])) # 1
    print(s.maxTurbulenceSize([0,8,45,88,48,68,28,55,17,24])) # 8
    print(s.maxTurbulenceSize([100,100,100])) # 1