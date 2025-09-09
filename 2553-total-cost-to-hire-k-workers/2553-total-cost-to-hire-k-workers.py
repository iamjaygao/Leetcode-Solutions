class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        left_heap = []
        right_heap = []
        n = len(costs)
        cost = 0

        left = 0
        right = n-1
        for i in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, costs[left])
                left += 1
            if left <= right:
                heapq.heappush(right_heap, costs[right])
                right -= 1
        
        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                cost += heapq.heappop(left_heap)
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                cost += heapq.heappop(right_heap)
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1
        return cost

