import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        # Step 1: Add the head of each list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy

        # Step 2: Keep popping the smallest element
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            # Step 3: Push the next node of the same list into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
