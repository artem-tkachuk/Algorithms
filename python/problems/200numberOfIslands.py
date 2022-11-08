class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        num_islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.recursiveDfs(grid, i, j)
                    num_islands += 1
        
        return num_islands

    def recursiveDfs(self, grid, i, j):
        grid[i][j] = '0'

        rowsTotal, colsTotal = len(grid), len(grid[0])

        steps = [
            [i - 1 >= 0, i - 1, j], # look up
            [j + 1 < colsTotal, i, j + 1],  # look right
            [i + 1 < rowsTotal, i + 1, j], # look down
            [j - 1 >= 0, i, j - 1]  # look left
        ] 
        
        for step in steps:
            [valid_step, k, r] = step
    
            if valid_step and grid[k][r] == '1':
                self.recursiveDfs(grid, k, r)

    def IterativeDfs(self, grid: list[list[str]], i: int, j: int):
            rowsTotal, colsTotal = len(grid), len(grid[0])
        
            queue = [(i, j)]
            steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # up, right, down, left

            while queue:
                row, col = queue.pop()
                grid[row][col] = '0'

                for (dr, dc) in steps:
                    r, c = row + dr, col + dc
                    valid_step = r in range(rowsTotal) and c in range(colsTotal)

                    if valid_step and grid[r][c] == '1':
                        queue.append((r, c))