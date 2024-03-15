#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        #Solution of implementing a Hash Set to keep track of current values and when duplicate is seen return True
        duplicateSet = set()
        for i in nums:
            if i in duplicateSet: #Means this is a duplicate!
                return True
            else:
                duplicateSet.add(i) #Not duplicate so add it to set to keep track
        return False