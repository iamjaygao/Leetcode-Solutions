class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell
            
            idx = bisect.bisect_left(potions, min_potion)
            result.append(n-idx)
        return result





            


