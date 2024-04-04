# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Requires recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #Recursion setup

        # if root is null, return null
        if not root:
            return None
        
        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp            

        #recursively inverting the sub-trees
        self.invertTree(root.left) #recursively on the left subtree
        self.invertTree(root.right) #recursively on the right subtree
        return root #finished recursion