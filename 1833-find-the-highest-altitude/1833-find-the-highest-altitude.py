class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = [0]
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            alts.append(alt)
        return max(alts)
            
            

