class Solution:
    def maxSubArray(self, nums):
        max_total = float('-inf')
        max_current = float('-inf')
        for num in nums:
            max_current = max(num, max_current +num)
            max_total = max(max_total, max_current)
      
        return max_total




        