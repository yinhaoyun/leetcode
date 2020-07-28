import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        t_counts = collections.Counter(tasks)
        cnt = sorted([c for c in t_counts.values()], reverse=True)
        most_freq = cnt[0] - 1
        spaces = most_freq * n
        for c in cnt[1:]:
            spaces -= min(most_freq, c)
        spaces = max(0, spaces)
        return len(tasks) + spaces


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], n=2))  # 8
print(s.leastInterval(["A", "A", "A", "B", "B", "B", "B"], n=2))  # 10
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], n=0))  # 6
print(s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))  # 16
