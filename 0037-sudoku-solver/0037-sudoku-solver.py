from typing import List, Tuple, Set, Dict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DIGITS = set("123456789")
        Cell = Tuple[int, int]

        #---------build neighbor-------
        neighbors: Dict[Cell, Set[Cell]] = {}
        for r in range(9):
            for c in range(9):
                cell = (r,c)
                nbrs = set()

                # row & column
                for k in range(9):
                    if k != c:
                        nbrs.add((r, k))
                    if k != r:
                        nbrs.add((k, c))
                # 3*3 box 
                br, bc = (r // 3) * 3, (c //3) * 3 
                for rr in range(br, br + 3):
                    for cc in range(bc, bc + 3):
                        if (rr, cc) != cell:
                            nbrs.add((rr, cc))
                neighbors[cell] = nbrs 
        # ----Initialize domains---------------
        domains: Dict[Cell, Set[str]] = {}

        def used_values(cell: Cell) -> set[str]:
            r, c = cell
            used = set()

            for k in range(9):
                if board[r][k] != ".":
                    used.add(board[r][k])
                if board[k][c] != ".":
                    used.add(board[k][c])
            
            br, bc = (r // 3) *3, (c // 3) * 3
            for rr in range(br, br + 3):
                for cc in range(bc, bc + 3):
                    if board[rr][cc] != ".":
                        used.add(board[rr][cc])
            return used
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    domains[(r, c)] = DIGITS - used_values((r,c))
        
        #------MRV------------
        def select_mrv() -> Cell:
            return min(domains, key = lambda cell: len(domains[cell]))

        #---------Forward checking-------
        def forward_check(cell: Cell, value: str):
            pruned = []
            for nbr in neighbors[cell]:
                if nbr in domains and value in domains[nbr]:
                    domains[nbr].remove(value)
                    pruned.append((nbr, value))
                    if len(domains[nbr]) == 0:
                        return False, pruned
            return True, pruned   

        def undo(pruned):
            for cell, value in pruned:
                if cell in domains:
                    domains[cell].add(value)
        
        #---------backtracking--------
        def backtrack() -> bool:
            if not domains:
                return True 
            cell = select_mrv()
            r,c = cell

            for value in sorted(domains[cell]):
                board[r][c] = value
                saved_domain = domains[cell]
                del domains[cell]

                ok, pruned = forward_check(cell, value)
                if ok and backtrack():
                    return True 
            
                # undo 
                undo(pruned)
                domains[cell] = saved_domain
                board[r][c] = "."
            return False
        backtrack()