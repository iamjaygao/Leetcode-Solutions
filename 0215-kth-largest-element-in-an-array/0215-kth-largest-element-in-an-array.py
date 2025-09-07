class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element using a min-heap of size k
        """
        min_heap = []
        for num in nums:
            # push the num to the min_heap
            heapq.heappush(min_heap, num)

            # if heap size exceed k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


        


