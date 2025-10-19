class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1: We are given an integer array, 
        2: return the answer, such that answer[i] = product all element except itself
        """
        n = len(nums)
        result = [1] * n
        # step 1: get the product of left side of the i
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]
        # step2: right part
        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result 

 