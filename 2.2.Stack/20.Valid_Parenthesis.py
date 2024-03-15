'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paren in s:
            if paren == '(' or paren == '{' or paren == "[": #opening parenthesis, simply add it to our array (aka stack)
                stack.append(paren)
            else: #This is triggered when we have a closing parenthesis for our 'paren' variable
                if len(stack) == 0: #nothing to pop, this means we're matching a closing paren with nothing and would get error. This if statement is to avoid popping nothing by checking first and returning false
                    return False

                openparen = stack.pop() #This pops the most recent open parenthesis in our stack, aka the most recent one that NEEDS to be closed
                if (paren == ")" and openparen == "(") or (paren == "}" and openparen == "{") or (paren == "]" and openparen == "["): #cross checking our closing parenthesis matches with our opening parenthesis
                    continue #matches so we continue the rest of the checks
                else:
                    return False #No match, thus return false
        if len(stack) == 0: #aka everything has been popped and matched properly, hence our stack is empty
            return True