# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node pointing to the head (helps handle edge cases)
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move 'first' n+1 steps ahead so that the gap between
        # 'first' and 'second' is n nodes
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until 'first' reaches the end
        while first:
            first = first.next
            second = second.next

        # 'second.next' is the node to remove
        second.next = second.next.next

        # Return the modified list
        return dummy.next
