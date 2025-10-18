class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        1: Given an array nums, integer k
        2: find three non-overlapping subarray of length k
        3: get the maximum sum
        4: return the starting position of each interval
        == choose three segment, each k long, non-overlapping, maximizing(sum1 + sum2 + sum3)
        """
        result = []
        n = len(nums)
        windows = [0] * (n - k +1) # build a new array used to store the sum of subarrays
        curr = sum(nums[:k])
        windows[0] = curr
        for i in range(1, len(windows)):
            curr += nums[k+i-1] - nums[i-1]
            windows[i] = curr
        
        # best left to each index
        left = [0] * len(windows)
        best = 0
        for i in range(len(windows)):
            if windows[i] > windows[best]:
                best = i
            left[i] = best
        # right best for each index
        right = [0] * len(windows)
        best = len(windows) - 1
        for i in range(len(windows)-1, -1, -1):
            if windows[i] >= windows[best]:
                best = i
            right[i] = best
        
        # sweep middle window and combine
        max_total = 0
        res = []
        for m in range(k, len(windows)- k):
            l = left[m-k]
            r = right[m + k]
            total = windows[l] + windows[m] + windows[r]
            if max_total < total:
                max_total = total
                res = [l, m, r]

        return res




        