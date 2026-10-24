# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = tail = ListNode()

        minHeap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(minHeap)

        while minHeap:
            _, i, node = heapq.heappop(minHeap)
            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummy.next
