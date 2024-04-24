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