# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        removePos = length - n 
        if removePos == 0:
            return head.next

        prev, cur = None, head
        for pos in range(removePos + 1):
            if pos == removePos:
                prev.next = cur.next
            
            prev, cur = cur, cur.next

        return head