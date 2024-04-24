# https://leetcode.com/problems/valid-anagram/description/
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# Initial (Original) Solution Using Hash Maps
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Hash Map is presumably the best way to do this, as you can record unique chars, along with how often they repeat
        #Initializing a dictionary
        char_arr = {}
        
        #Iterating through the first string, adding its unique chars to the hash map, along with incrementing that unique chars value by 1 if its a repeat char
        for char in s:
            if char in char_arr:
                char_arr[char] += 1 #incrementing the value if it already exists
            else:
                char_arr[char] = 1 #Adding the unique char to the map
        
        #Iterating through the second string and checking if its character exists in the Hash Map, if it doesn't then we know its already not an Anagram and return False
        # Otherwise, if it exists, decrease its value (count) by 1, and if that coutn hits, 0, pop it from the array (important at the end when checking length of the Hash Map)
        for char in t:
            if char in char_arr:
                char_arr[char] -= 1
                if char_arr[char] == 0:
                    char_arr.pop(char)
            else:
                return False
        
        # If len of hash map is 0, this means we successfully popped all the chars, which means the second string is an anagram of the first string, thus return true
        if len(char_arr) == 0:
            return True
        else:
            return False

# NeetCode Solution 1 O(s+t) time complexity)
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        #Quick Check possible at the very beginning, simply check if the two strings have the same length, if not, we know its not possible to be an anagram
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # note cannot be countS[s[i]] = 1 + countS(s[i]) because countS(s[i]) may not exist already yet, so must use get( , 0) <= 0 is default value
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            if countS[c] != countT.get(c, 0): #once again we use get here just in case that character does NOT exist in T
                return False
        
        #Went through all the checks and loops, no return Falses or exiting early, thus it is an anagram
        return True

# NeetCode Solution 2, trying to get O(1) time compelexity
# Apparently some interviewers can see that sorting (depending on the library you use), is at best O(1) time complexity, so if we were to sort the two strings, then do direct comparison, it would obviously be the same string
#   if it was an anagram, thus we can quickly return true or false, and have O(1) time complexity
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    #Possibly interviewer will ask you to write out your own sorting function