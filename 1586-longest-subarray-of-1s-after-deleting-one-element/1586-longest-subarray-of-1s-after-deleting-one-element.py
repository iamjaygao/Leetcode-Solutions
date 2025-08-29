class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        mx_len = 0
        k = 1

        for right in range(n):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            mx_len = max(mx_len, right - left)
        return mx_len

