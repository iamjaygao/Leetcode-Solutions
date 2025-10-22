class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count.items(), key = lambda x : x[1], reverse = True)
        result = []
        for key, value in sorted_count:
            result.append(key)
            if len(result) == k:
                return result
        
            



        