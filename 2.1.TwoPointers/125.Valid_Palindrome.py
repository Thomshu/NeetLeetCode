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
    
    #Alternative Solution without built in functions like isalnum() (using ASCII values)
    #Alphanumerical function
    def alphaNum(self, c):
        #ord(c) function to get the ASCII value of the character
        # This will return true if its alphanumeric, otherwise returns false
        return ((ord('A') <= ord(c) and ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) and ord(c) <= ord('z')) or
                ord('0') <= ord(c) and ord(c) <= ord('9'))


    def isPalindrome(self, s: str) -> bool:
        l = 0 #Starting at the beginning index
        r = len(s)-1 # end index

        #check and converge from beginning to end.
        while l < r:
            while l < r and not self.alphaNum(s[l]): #Have to use the self keyword in python to call another function within an object
                l+=1
            while r > l and not self.alphaNum(s[r]):
                r-=1
                
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r -1

        return True