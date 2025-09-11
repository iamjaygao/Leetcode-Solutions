class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return 0 if n == 0 else cost[0]

        prev2 = 0
        prev1 = 0

        for i in range(2, n+1):
            current = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2 = prev1
            prev1 = current
        return prev1
