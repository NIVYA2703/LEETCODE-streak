from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])      
        arr = []
        for row in grid:
            arr.extend(row)
        k %= (m * n)
        arr = arr[-k:] + arr[:-k]
        result = []
        index = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[index])
                index += 1
            result.append(row)
        return result
