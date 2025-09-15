class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create DP table with dimnesions (m+1) * (n+1)
        # dp[i][j] = min operations to convert word1[0:i] to word2][0:j]  
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case1: Convert empty string to word2[0][j]--insert j characters
        for j in range(n+1):
            dp[0][j] = j
        
        # Base case2: Convert word1[0:i] to empty--delete i characters
        for i in range(m+1):
            dp[i][0] = i
        
        # Fill the DP table
        for i in range(1, m+1):
            for j in range(1, n+1):

                # characters match, no operation needed
                # Cost = previous substring conversion cost
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                else:    
                    # Characters don't match, choose minimum of three operations
                    # insert: dp[i][j-1] + 1 (insert character to match word2[j-1])
                    # delete: dp[i-1][j] + 1 (delete word1[i-1])
                    # replace: dp[i-1][j-1] +1 (replace word1[i-1] with word2[j-1]
                    dp[i][j] = 1+ min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) 
        
        return dp[m][n]
        