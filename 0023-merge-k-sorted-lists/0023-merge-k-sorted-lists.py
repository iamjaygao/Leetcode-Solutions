# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for head in lists:
            current = head
            while current:
                heapq.heappush(heap, current.val)
                current = current.next
        dummy = ListNode(0)
        current = dummy
        while heap:
            current.next = ListNode(heapq.heappop(heap))
            current = current.next
        return dummy.next

       