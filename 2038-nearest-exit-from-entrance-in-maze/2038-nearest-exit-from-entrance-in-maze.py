class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # find the size of row and column
        m = len(maze)
        n = len(maze[0])

        # q
        q = deque()

        # push the entrance to the queue and mark it as visited
        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = '+'

        # diractions 
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x, y, steps = q.popleft()
            if (x == 0 or x == m-1 or y == 0 or y == n-1) and steps > 0:
                return steps
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if  0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'
                    q.append((nx,ny, steps +1))
        return -1  
        











        
        