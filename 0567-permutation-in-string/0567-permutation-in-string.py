class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        count1 = Counter(s1)
        windows = Counter()
        for i, char in enumerate(s2):
            windows[char] += 1
            if i >= n1:
                leftchar = s2[i-n1]
                windows[leftchar] -=1
                if windows[leftchar] == 0:
                    del windows[leftchar]
            if windows == count1:
                return True
        return False


            


        


      
