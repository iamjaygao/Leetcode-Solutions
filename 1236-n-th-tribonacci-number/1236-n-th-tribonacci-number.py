class Solution:
    def tribonacci(self, n: int) -> int:
        # handle the base case
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a,b,c = 0, 1, 1

        for i in range(3, n+1):
            new_val = a + b + c
            a = b
            b = c
            c = new_val
        return c
        
