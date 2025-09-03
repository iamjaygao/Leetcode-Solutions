class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()
        q.append((entrance[0], entrance[1], 0))

        # list of lists = 2d grad
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            x, y, steps = q.popleft()
            if (x == 0 or x == m-1 or y == 0 or y == n-1) and steps > 0:
                return steps
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx >= 0 and nx < m and ny >= 0 and ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'
                    q.append((nx, ny, steps + 1))

        return -1












        
        