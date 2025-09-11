class Solution:
    def tribonacci(self, n: int) -> int:
        # handle the base case
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # initialize dp array of size n+1 
        # initialize with zeros for clean state and defined values
        dp = [0]* (n + 1)

        # set the known base values
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        # bottom-up computation
        for i in range(3,n+1):
            dp[i] = dp[i-1]+ dp[i-2] + dp[i-3]
        
        # return the nth tribonacci number
        return dp[n]

        