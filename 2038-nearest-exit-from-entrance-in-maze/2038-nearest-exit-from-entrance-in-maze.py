class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # initialize 
        # get the maze dimensions
        m = len(maze)
        n = len(maze[0])

        # define movement directions
        directions = [(1,0),(-1,0),(0,1),(0,-1)] #right, left, down, up

        # BFS queue
        q = deque()
        q.append((entrance[0], entrance[1], 0)) #(row, column, steps)

        # list of lists = 2d grad, mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+' 

        # BFS traversal 
        while q:

            # get current position and step count
            x, y, steps = q.popleft()

            # check if current cell is a valid exit
            # note that the 'and' 的运算符的优先级比 ‘or’ 高， 所有'or' 需要用()
            if (x == 0 or x == m-1 or y == 0 or y == n-1) and steps > 0:
                return steps # Returns the steps to nearest exit

            # Explore all four dirctions using tuple unpacking
            for dx, dy in directions:

                # calculate new position
                nx, ny = x + dx, y + dy

                # check if new position is within bounds and accessible
                if nx >= 0 and nx < m and ny >= 0 and ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+' # mark as visited
                    q.append((nx, ny, steps + 1)) # add to queue

        return -1 # no path to exit found












        
        