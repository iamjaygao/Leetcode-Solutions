class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        1: Given an integer array: nums, int: k
        2: Asked to split the array into k non-empty subarray
        3: return the largest sum which is as minimum as possible
        """
        n = len(nums)
        if n == k:
            return max(nums)
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (right + left) // 2
            if self.can_split(nums, k, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def can_split(self, nums, k, max_sum):
        curr_sum = 0
        count = 1
        for num in nums:
            if curr_sum + num > max_sum:
                count += 1
                curr_sum = num
                if count > k:
                    return False
            else:
                curr_sum += num
        return True





        