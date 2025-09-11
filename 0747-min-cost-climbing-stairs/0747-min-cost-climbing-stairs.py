class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # handle the edge cases
        if n == 0:
            return 0
        if n == 1:
            return cost[0] # only one step, must pay to climb from it
        
        # initialize DP array
        # size n+1 to store costs for steps 0 through n
        # initialize wit zeros for clean state
        dp = [0] * (n + 1)

        # set base case, note that reaching there costs 0, but leave there to higher step cost cost[i]
        dp[0] = 0       #cost 0 to reach step 0 
        dp[1] = 0       #cost 0 to reach step 1

        for i in range(2, n+1):
            from_prew = dp[i-1] + cost[i-1]
            from_two_back = dp[i-2] + cost[i-2]
            dp[i] = min(from_prew, from_two_back)

        # return the cost to reach the top (step n)
        return dp[n]