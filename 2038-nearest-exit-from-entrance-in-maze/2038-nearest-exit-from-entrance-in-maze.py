class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        q = deque()
        # push the entrance and step where is 0 to the q
        q.append((entrance[0], entrance[1], 0 ))
        maze[entrance[0]] [entrance[1]] = '+'

        directions = [(-1,0), (1,0),(0,-1),(0,1)]
        while q:
            row, col, steps = q.popleft()
            if (row == 0 or row == m-1 or col == 0 or col == n-1) and steps > 0:
                return steps
            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                if nrow >= 0 and nrow < m and ncol >=0 and ncol < n and maze[nrow][ncol] == '.':
                    maze[nrow][ncol] = '+'
                    q.append((nrow, ncol, steps+1))
        return -1
            











        
        