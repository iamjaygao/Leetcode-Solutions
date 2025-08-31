class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = Counter(tuple(row) for row in grid)

        count = 0
        for j in range(n):
            col_content = tuple(grid[i][j] for i in range(n))
            count += row_count[col_content]
        
        return count


        
        