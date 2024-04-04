#https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#For solution 2
from collections import deque

class Solution:
    #Solution 1: Recursive Depth First Search
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0 #max depth of 0 if root is null

        #The 1 is indicating the root itself, which gives a depth of 1 as a base, add this to the recursion and it adds up the depth for us
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # 2 Other Solutions without Recursion
    #Solution 2: Breadth First Search (BFS) 
    # Logic => Traversing each level by level (horizontally) until we get to the last level and can't continue anymore
    # Counting the levels we have, generally done using a QUEUE or DEQUEUE
        # Put the root in, and then replace that root with its children, for each level
    def maxDepth2(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q: #keep going until the queue is empty
            
            #going through the queue to see the elements, remove all of those elements at this level and add their respective children
            for i in range(len(q)): 
                node = q.popleft() #popping the nodes to the left of the queue, and adding nodes to the right of the queue
                if node.left: #left node not null, add to queue
                    q.append(node.left)
                if node.right: #similarly if right node not null, add to queue
                    q.append(node.right)
                
            level += 1
        
        return level

    #Solution 3: Iterative DFS (Pre-order DFS)
    #Requires Stack Data Structure
    #Processes each node and its children (from left side to right first => pre order)
    # Stack will contain the nodes themselves, along with their corresponding depth
        # pop the node and add its children like the queue in solution 2
    # Visits every single node and returns the greatest depth
    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        
        stack = [[root, 1]] # (node, depth)
        result = 0
        
        while stack:
            node, depth = stack.pop() #pop the current root and append its children if possible
            
            if node: #if node is null, we won't do anything to it. Purpose of this if statement is when we .extend(), we are potentially adding null left and right nodes, so this takes care of that case
                # As well, say if the original root is null (aka empty tree), we will never execute this case, and result = 0 aka depth is 0
                result = max(result, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        
        return result