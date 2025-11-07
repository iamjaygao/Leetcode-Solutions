class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Given: nums:list, list[i]represents the max length of a froward jump from index i
        Return the minimum number of jumps to reach n-1 (The last element)
        dp
        """
        n = len(nums)
        end = 0
        largest = 0
        step = 0
        for i in range(n-1):
            largest = max(largest, nums[i] + i)
            if i == end:
                step += 1
                end = largest
        return step
               

            

        