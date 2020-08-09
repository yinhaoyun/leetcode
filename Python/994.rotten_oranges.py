from itertools import product
from typing import List, Tuple, Dict
from collections import deque


class Solution:
    """
    https://leetcode.com/problems/rotting-oranges/
    """
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2
    DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def __init__(self):
        self.orangesRotting = self.clean_bfs

    # Use graph
    # 68ms, 41%
    def my_graph_solution(self, grid: List[List[int]]) -> int:
        cy, cx, queue, fresh = len(grid), len(grid[0]), deque(), 0
        conn_dict = dict()
        for y, x in product(range(cy), range(cx)):
            if grid[y][x] == Solution.FRESH:
                fresh += 1
            if grid[y][x] == Solution.ROTTEN:
                queue.append((x, y))
            if grid[y][x]:
                for dx, dy in Solution.DIRS:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < cx and 0 <= ny < cy and grid[ny][nx]:
                        conn_dict.setdefault((x,y),set()).add((nx, ny))
                        conn_dict.setdefault((nx,ny),set()).add((x, y))
        # print(f"conn_dict={conn_dict}")
        # print(f"queue={queue}")

        minute = 0
        while queue:
            minute += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) not in conn_dict:
                    continue

                # BFS
                to_be_del_conn = []
                for nx, ny in conn_dict[(x, y)]:
                    if grid[ny][nx] == Solution.FRESH:
                        fresh -= 1
                        if fresh == 0:
                            return minute
                        grid[ny][nx] = Solution.ROTTEN
                        queue.append((nx, ny))
                        to_be_del_conn.append((x, y, nx, ny))

                # Remove used path
                for x, y, nx, ny in to_be_del_conn:
                    conn_dict[(x, y)].remove((nx, ny))
                    conn_dict[(nx, ny)].remove((x, y))
        return -1 if fresh else max(minute - 1, 0)


    """
    https://leetcode.com/problems/rotting-oranges/discuss/781642/Python-clean-BFS-solution-explained
    48ms, 93%
    """
    def clean_bfs(self, grid: List[List[int]]) -> int:
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        # print(f"grid={grid}, m={m}, n={n}")
        for y, x in product(range(m), range(n)):
            if grid[y][x] == Solution.FRESH:
                fresh += 1
            if grid[y][x] == Solution.ROTTEN:
                queue.append((x, y))

        minute = 0
        while queue:
            minute += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in Solution.DIRS:
                    if 0 <= x + dx < n and 0 <= y + dy < m and grid[y + dy][x + dx] == Solution.FRESH:
                        # print(f"minute={minute}, ({x+dx},{y+dy}) get rotten, fresh={fresh}")
                        grid[y + dy][x + dx] = Solution.ROTTEN
                        queue.append((x + dx, y + dy))
                        fresh -= 1
                        if fresh == 0:
                            return minute
        # print("last fresh=", fresh)
        return -1 if fresh else max(minute - 1, 0)

    def my_1st_graph(self, grid: List[List[int]]) -> int:
        rotten = 0
        graph = dict()
        state = dict()
        check_q = []
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val in (Solution.FRESH, Solution.ROTTEN):
                    graph.setdefault((x, y), set())
                    Solution.check_and_connect((x, y), grid, graph)
                    state[(x, y)] = val
                if val == Solution.ROTTEN:
                    rotten += 1
                    check_q.append((x, y))
        print("graph:", graph)
        minute = 0
        print("minute=", minute, ", check_q=", check_q)
        if rotten == len(graph):
            return 0
        while len(check_q):
            next_q = []
            minute += 1
            for x, y in check_q:
                # print("check: ", x, y)
                if graph.get((x, y)) is None:
                    continue
                for conn in graph[(x, y)]:
                    # print("conn:", conn)
                    if state[conn] == Solution.FRESH:
                        state[conn] = Solution.ROTTEN
                        rotten += 1
                        next_q.append(conn)
            check_q = next_q
            # print("minute=", minute, ", check_q=", check_q)
        # print("rotten=", rotten, ", len(graph)=", len(graph))
        if rotten != len(graph):
            return -1
        else:
            return minute - 1

    @staticmethod
    def check_and_connect(coord: Tuple[int], grid: List[List[int]], graph: Dict) -> None:
        x = coord[0]
        y = coord[1]
        if x < len(grid[0]) - 1 and grid[y][x + 1] in (Solution.FRESH, Solution.ROTTEN):
            graph.setdefault((x, y), set()).add((x + 1, y))
            graph.setdefault((x + 1, y), set()).add((x, y))
        if y < len(grid) - 1 and grid[y + 1][x] in (Solution.FRESH, Solution.ROTTEN):
            graph.setdefault((x, y), set()).add((x, y + 1))
            graph.setdefault((x, y + 1), set()).add((x, y))


if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
    print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
    print(s.orangesRotting([[0, 2]]))  # 0
    print(s.orangesRotting([[1, 2]]))  # 1
    print(s.orangesRotting([[1], [2]]))  # 1
