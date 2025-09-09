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
            min_potion = (success + spell -1) // spell
            
            left, right = 0, n

            while left < right:
                mid = (right + left) // 2
                
                if potions[mid] < min_potion:
                    left = mid + 1
                else:
                    right = mid
            result.append(n-left)
        return result

       



            


