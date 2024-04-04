#https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Solution 1: Recursive Depth First Search
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0 #max depth of 0 if root is null

        #The one is indicating the root itself, which gives a depth of 1 as a base, add this to the recursion and it adds up the depth for us
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))