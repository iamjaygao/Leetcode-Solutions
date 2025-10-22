class Solution:
    def maxSubArray(self, nums):
        total = float("-inf")
        per_sum = float("-inf")
        for num in nums:
            per_sum = max(per_sum + num, num)
            total = max(total, per_sum)
        return total 





        