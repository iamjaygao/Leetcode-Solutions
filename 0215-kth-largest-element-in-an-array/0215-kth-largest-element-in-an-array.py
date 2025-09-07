class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element using a min-heap of size k
        """
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]
        


