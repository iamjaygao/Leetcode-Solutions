class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            skip_i = dp[i-1]
            take_i = dp[i-2] + nums[i]
            dp[i] = max(skip_i, take_i)
        return dp[n-1]    