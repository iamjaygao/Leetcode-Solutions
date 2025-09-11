class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            skip = dp[i-1] + cost[i-1]
            take = dp[i-2] + cost[i-2]
            dp[i] = min(skip, take)
        return dp[n]

