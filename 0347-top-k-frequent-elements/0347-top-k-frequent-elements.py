class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = sorted(count.items(), key = lambda x: x[1], reverse = True)
        result = []
        for i in range(k):
            k, v = res[i]
            result.append(k)
        return result
 
        

        