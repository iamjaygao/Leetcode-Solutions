class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        window = Counter()
        found = 0
        res = [-1, -1]
        len_res = float("inf")
        left = 0
        for right, char in enumerate(s):
            if char in count:
                window[char] = window.get(char, 0) + 1
                if window[char] == count[char]:
                    found += 1
            while found == len(count):
                if right - left + 1 < len_res:
                    len_res = right - left + 1
                    res = [left, right]
                left_char = s[left]
                if left_char in count:
                    window[left_char] -= 1
                    if window[left_char] < count[left_char]:
                        found -= 1
                left += 1
            l ,r = res
        return s[l: r+1] if len_res != float("inf") else ""
          











 


             




        