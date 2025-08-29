class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        alt = 0

        for g in gain:
            alt += g
            max_alt = max(alt,  max_alt)
        return max_alt


            

