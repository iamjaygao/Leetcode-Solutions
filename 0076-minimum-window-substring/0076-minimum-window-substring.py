class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return the smallest contiguous substring,such that every character in t is includede in it
        # including duplicates, 

        m, n = len(s), len(t)   # get the size of s and n
        count = Counter(t)      # et all elements in t and its frequency
        windows = {}            # ceeate a dict to save the element
        found = 0               # how many requeired char been found so far
        res = [-1, -1]
        res_len = float("inf")
        left = 0
        for right, char in enumerate(s):
            if char in count:
                windows[char] = windows.get(char, 0) + 1
            if char in count and windows[char] == count[char]:
                found += 1
            while found == len(count):
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res =[left, right]
                left_char = s[left]
                if left_char in count:
                    windows[left_char] -= 1
                if left_char in count and windows[left_char] < count[left_char]:
                    found -= 1
                left += 1
        l, r = res
        return s[l :r+1] if res_len != float("inf") else ""    
                








 


             




        