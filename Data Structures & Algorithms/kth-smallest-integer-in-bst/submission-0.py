# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        arr = []
        
        count = 1

        curr = root        
        while stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if k == count:
                return curr.val
            count += 1

            curr = curr.right

            

