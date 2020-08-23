from typing import List


# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
class Solution:

    # https://leetcode.com/problems/most-visited-sector-in-a-circular-track/discuss/806814/JavaC%2B%2BPython-From-Start-to-End
    # Brilliant one
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        _from, to = rounds[0], rounds[-1]
        if to >= _from:
            result = list(range(_from, to + 1))
        else:
            result = list(range(1, to + 1)) + list(range(_from, n + 1))
        return result

    # Runtime: 40 ms, faster than 100.00%
    def my_stupid(self, n: int, rounds: List[int]) -> List[int]:
        # print(f"mostVisited: n={n}, rounds={rounds}")
        run_sectors = [(s1 - s2) % n for s1, s2 in zip(rounds[1:], rounds[:-1])]
        sectors_sum = sum(run_sectors) + 1
        # print(f"run_sectors={run_sectors}, sectors_sum={sectors_sum}")
        mod = sectors_sum % n
        if mod == 0:
            mod = n
        if rounds[0] + mod <= n:
            result = range(rounds[0], rounds[0] + mod)
        else:
            result = list(range(1, rounds[0] + mod - n)) + list(range(rounds[0], n + 1))

        return list(result)


s = Solution()
print(s.mostVisited(n = 4, rounds = [1,3,1,2]))  # [1,2]
print(s.mostVisited(n = 2, rounds = [2,1,2,1,2,1,2,1,2]))  # [2]
print(s.mostVisited(n = 7, rounds = [1,3,5,7]))  # [1,2,3,4,5,6,7]
print(s.mostVisited(n = 4, rounds = [3, 1, 3, 1]))  # [1, 3, 4]
print(s.mostVisited(2, [1, 2, 1]))  # [1]
print(s.mostVisited(3, [2,1,2,1,3,2,3,1,2,3,1,3,1,2,3,1,3,2,3,2,1,2,3,1,3]))  # [2, 3]