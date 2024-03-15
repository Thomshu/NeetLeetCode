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