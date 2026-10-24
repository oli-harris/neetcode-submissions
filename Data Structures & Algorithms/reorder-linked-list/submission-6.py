# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the midpoint
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        second = slow.next
        mid.next = None

        # 2. Reverse second half
        prev, cur = None, second
        while cur:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        
        tail = prev

        # 3. Merge together
        while tail:
            tmp1, tmp2 = head.next, tail.next
            head.next = tail
            tail.next = tmp1
            head, tail = tmp1, tmp2
