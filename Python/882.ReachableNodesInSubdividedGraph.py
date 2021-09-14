import heapq
from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0
        while pq:
            # print(f"pq={pq}")
            d, node = heapq.heappop(pq)
            # print(f"cur={node}, d={d}")
            if d > dist[node]:
                # print("skip")
                continue
            ans += 1
            # print(f"ans+1={ans}\n")
            for nei, weight in graph[node].items():
                # print(f"connect to {nei}, w = {weight}")
                v = min(weight, maxMoves - d)
                used[node, nei] = v
                # print(f"put {v} to used[{node}, {nei}])")
                # print(f"used={used}")

                d2 = d + weight + 1
                if d2 < dist.get(nei, maxMoves + 1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2
                    # print(f"dist[{nei}] = {d2}")
                    # print(f"dist={dist}")

                # print()
            # print()
        for u, v, w in edges:
            ans += min(w, used.get((u,v), 0) + used.get((v,u), 0))
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3)) # 13
    print(s.reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4)) # 23
    print(s.reachableNodes([[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], 17, 5)) # 1
    print(s.reachableNodes([[1,3,23],[3,5,19],[3,6,17],[1,5,14],[6,7,20],[1,4,10],[1,6,0],[3,4,20],[1,7,4],[0,4,10],[0,7,9],[2,3,3],[3,7,9],[5,7,4],[4,5,16],[0,1,16],[2,6,0],[4,7,11],[2,5,14],[5,6,22],[4,6,12],[0,6,2],[0,2,1],[2,4,22],[2,7,20]],
                           19, 8))