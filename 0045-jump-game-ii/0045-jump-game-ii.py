class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Given: nums:list, list[i]represents the max length of a froward jump from index i
        Return the minimum number of jumps to reach n-1 (The last element)
        dp
        """
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n-1]
 
            

            

        