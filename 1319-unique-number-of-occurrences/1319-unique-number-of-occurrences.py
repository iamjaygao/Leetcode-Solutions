class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter()
        for a in arr:
            count[a] += 1
        return len(list(count.values())) == len(set(count.values()))

