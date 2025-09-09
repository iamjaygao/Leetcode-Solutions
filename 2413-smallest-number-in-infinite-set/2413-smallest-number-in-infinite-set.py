class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = []                 #min_heap for numbersa dded via addback
        self.in_heap = set()           # fast existence checking for heap numbers
        self.current_min = 1           # next avaiable natural number

    def popSmallest(self):
        """
        :rtype: int
        """
        # priority: return smallest from addedd-back numbers
        if self.heap:       
            smallest = heapq.heappop(self.heap)
            self.in_heap.remove(smallest)
            return smallest
        
        # if no added_back numbers, retuen the next natural number
        else:
            smallest = self.current_min
            self.current_min += 1           # move to next natural number
            return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        # only procrss if:
        # 1, num < current_min( was previously popped)
        # 2, num not in heap (avoid dupicates)
        if num < self.current_min and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)