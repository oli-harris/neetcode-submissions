"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # depth first search
        clones = {node: Node(node.val)}
        stack = [node]

        while stack:
            n1 = stack.pop() 
            c1 = clones[n1]
            
            for n2 in n1.neighbors:
                if n2 not in clones:
                    c2 = Node(n2.val)
                    clones[n2] = c2
                    stack.append(n2)
                else:
                    c2 = clones[n2]

                c1.neighbors.append(c2)



        return clones[node]

        