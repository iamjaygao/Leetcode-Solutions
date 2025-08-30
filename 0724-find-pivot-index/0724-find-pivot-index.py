class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        for i in range(len(nums)):
            sum_left = sum(nums[:i])
            if nums[i] == total - sum_left * 2:
                return i
        return -1
            
           