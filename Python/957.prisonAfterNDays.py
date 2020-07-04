from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        initial = list(cells)
        new_cells = [0] * len(cells)

        def one_day(cells: List[int]) -> List:
            for i in range(1, len(cells) - 1):
                new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            new_cells[0] = new_cells[-1] = 0
            # print(new_cells)

        one_day(cells)
        cells, new_cells = new_cells, cells
        initial = list(cells)
        simple_n = 0
        N -= 1
        for n in range(0, N):
            one_day(cells)
            cells, new_cells = new_cells, cells
            if initial == cells:
                simple_n = n + (N % (n + 1))
            if simple_n and n == simple_n:
                break

        return cells


s = Solution()
print(s.prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7))  # [0, 0, 1, 1, 0, 0, 0, 0]
print(s.prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000))  # [0,0,1,1,1,1,1,0]
