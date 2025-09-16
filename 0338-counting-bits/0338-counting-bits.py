class Solution:
    def countBits(self, n: int) -> List[int]:
        # initialize DP array with zeros
        dp = [0] * (n+1)

        # Iterate through all number from 1 to n
        for i in range(1, n+1):
            # key insight:
            # dp[i] = dp[i >> 1] + (i & 1)
            #
            # i >> 1: right shift by 1 (equvialent to i // 2)
            # i & 1: returns 1 if i is ood, 0 if even
            #
            # For even numbers: i & 1 = 0, so dp[i] = dp[i//2] 
            # For odd numbers: i & 1 = 1, so dp[i] = dp[i//2] + 1
            dp[i] = dp[i>>1] + (i & 1)
        return dp

