class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs.sort(key = lambda x : x[1], reverse = True)

        min_heap = []
        result = 0
        curr_sum = 0

        for n1, n2 in pairs:
            heapq.heappush(min_heap, n1)
            curr_sum += n1

            if len(min_heap) > k:
                smallest = heapq.heappop(min_heap)
                curr_sum -= smallest
            
            if len(min_heap) == k:
                score = curr_sum * n2
                result = max(score, result)
        return result
        

        