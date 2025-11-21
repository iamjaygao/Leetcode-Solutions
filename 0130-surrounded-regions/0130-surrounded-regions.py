class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        m, n = len(board), len(board[0])
        dirct = {(-1, 0), (1, 0),(0,1),(0,-1)}
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and board[i][j] == "O"):
                return
            board[i][j] = "#"
            for dc, dr in dirct:
                nc = dc + i
                nr = dr + j
                dfs(nc, nr)

        for i in range(n):
            dfs(0,i)
            dfs(m-1, i)
        for j in range(m):
            dfs(j, 0)
            dfs(j,n-1)
      
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        return board 


