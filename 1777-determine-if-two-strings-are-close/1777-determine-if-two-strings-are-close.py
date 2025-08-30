class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        return count1.keys() == count2.keys() and sorted(list(count1.values())) == sorted(list(count2.values()))
        
        
        