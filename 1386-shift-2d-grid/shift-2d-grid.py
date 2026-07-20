class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])

        new_grid = [[0]*n for _ in range(m)]

        k %= (m*n)

        for i in range(m):
            for j in range(n):

                position = i*n+j

                new_position = (position + k) % (m *n)

                new_row = new_position // n

                new_col = new_position % n

                new_grid[new_row][new_col] = grid[i][j]

        return new_grid