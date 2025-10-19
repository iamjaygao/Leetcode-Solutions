class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        result = set()
        max_length = 0
        for right in range(len(s)):
            while s[right] in result:
                result.remove(s[left])
                left += 1
            result.add(s[right])
            max_length = max(max_length, right-left+1)
        return max_length
               








        