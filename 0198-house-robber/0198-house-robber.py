class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # handle the edge cases
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # initialize DP array
        # dp[i] represents max profit from first to i+1 houses
        dp = [0] * (n)

        # set base cases
        dp[0] = nums[0]     #only one house
        dp[1] = max(nums[0], nums[1]) # two houses, choose the better one

        # Bottom-up computation
        for i in range(2, n):

            # two choice
            # 1, skip current house, keep profit from previous house dp[i-1]
            # 2, rob currtn house, add current money to profit from i-2 (dp[i-2] + nums[i] )
            skip = dp[i-1]
            take = dp[i-2] + nums[i]
            dp[i] = max(skip, take)

        # return the maximum profit
        return dp[n-1]
        
        