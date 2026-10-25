# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {v: i for i, v in enumerate(inorder)}

        if not preorder or not inorder:
            return None
    
        def dfs(pl, pr, il, ir):
            if pl >= pr:
                return None

            root = TreeNode(preorder[pl])
            inIndex = inorderIdx[preorder[pl]]
            left = inIndex - il 

            root.left = dfs(pl + 1, pl + 1 + left, il, inIndex) # preorder[1 : inIndex + 1], inorder[:inIndex]
            root.right = dfs(pl + 1 + left, pr, inIndex + 1, ir) # preorder[inIndex + 1 :], inorder[inIndex + 1 :]

            return root
        
        return dfs(0, len(preorder), 0, len(preorder))
