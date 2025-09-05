class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get the size of the grid
        m, n = len(grid), len(grid[0])

        # edge case, if not grid nor grid[0] 
        if not grid or not grid[0]:
            return -1
        # initial the q and fresh_count 

        q = deque()
        fresh_count = 0

        # four directions
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # find the rotten orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    # add rotten orange with initial time = 0
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh_count += 1

        # edge case: no fresh oranges to infect or all of the orange are rotten
        if fresh_count == 0:
            return 0
        # edge case: fresh oranges exist but no rotten orange to start infection
        if not q and fresh_count > 0:
            return -1
        
        # track the max infection time
        max_time = 0

        # multiple-source BFS: process all rottrn oranges simultaneously 
        while q:
            a, b, time  = q.popleft()
            max_time = max(max_time, time) #update the max time

            # check all four directions for fresh oranges
            for x,y in directions:
                new_row, new_col = a + x, b + y
                
                # check boundaries and if the orange is fresh
                if  0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    # infect the fresh orange
                    grid[new_row][new_col] = 2
                    fresh_count -= 1

                    # add the new rotten orange to the q and time + 1
                    q.append((new_row, new_col, time + 1))

        # check if all fresh oranges were infected:
        return max_time if fresh_count == 0 else -1





        
        

        


        