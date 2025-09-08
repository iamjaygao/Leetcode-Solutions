class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = []
        self.in_heap = set()
        self.current_min = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.in_heap.remove(smallest)
            return smallest

        smallest = self.current_min
        self.current_min += 1
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.current_min and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)