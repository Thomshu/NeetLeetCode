#https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head

        while current_node != None:
            temp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp
        
        return prev_node
