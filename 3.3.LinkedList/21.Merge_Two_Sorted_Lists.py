#https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headnode = current = ListNode()
        
        while list1 and list2: #iterates as long as list1 and list2 are not empty
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        #Now we are out of the loop, this means that one or even both of the lists are empty, thus we will do an if statement here if they are not empty
        if list1 or list2:
            if list1:
                current.next = list1
            else:
                current.next = list2
            
        return headnode.next #have to do .next since our original headnode was an initialized ListNode() 

#Time: O(n)
#Space: O(1)