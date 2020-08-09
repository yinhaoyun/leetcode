from typing import List, Tuple, Dict


class Solution:
    """
    https://leetcode.com/problems/rotting-oranges/
    """
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

    def __init__(self):
        self.orangesRotting = self.my_1st_graph

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
            minute +=1
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
    print(s.orangesRotting([[1],[2]]))  # 1
