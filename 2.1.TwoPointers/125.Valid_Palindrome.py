'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #We know that a palindrome must read backwards and forwards, therefore a good solution is two pointers (start and end) reading towards each other and comparing
        l = 0 #Starting at the beginning index
        r = len(s)-1 # end index

        #check and converge from beginning to end.
        while l < r:
            #Converting to lowercase as the examples have upper and lowercase letters
            a = s[l].lower() 
            b = s[r].lower()
            if a.isalnum() and b.isalnum(): #Important line as there are spaces, commas, special characters in the sentences.
                if a != b:
                    return False
                else:
                    l = l+1
                    r = r-1
                    continue

            # These two lines here adjust the i and j value accordingly if they encounter non alphanumeric characters
            if a.isalnum() == False:
                l += 1
            if b.isalnum() == False:
                r -= 1

            #Shorter more efficient code for the two if statements above
            #l = l + (not a.isalnum())
            #r = r - (not b.isalnum())

        return True