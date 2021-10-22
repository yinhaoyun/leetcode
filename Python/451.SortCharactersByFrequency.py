from collections import Counter
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        pq = []
        for a, freq in cnt.items():
            pq += [(freq, a)]

        pq.sort(reverse=True)
        return "".join(a * freq for freq, a in pq)

    def frequencySort_pq(self, s: str) -> str:
        cnt = Counter(s)
        pq = []
        for k, v in cnt.items():
            heapq.heappush(pq, (-v, k))

        res = ""
        while pq:
            freq, alpha = heapq.heappop(pq)
            res += alpha * (-freq)
        return res

