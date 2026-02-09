'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false


Use a Stack and a Hashmap
'''
class Solution:
    def ValidParentheses(self, s: str) -> bool:
        # stack holds opening parens
        stack = [] 
        # valid pairings of open and close parens
        matching = {"(":")", "{":"}", "[":"]"}

        # look at each bracket
        for bracket in s:
            # if the bracket is an opening bracket
            if bracket in matching:
                # push it to the stack
                stack.append(bracket)
            else:
                # if a closing bracket, but there is no opening bracket on the stack
                if not stack:
                    return False
                # if the top of the stacks closing bracket doesnt match the closing bracket we see
                if matching[stack.pop()] != bracket:
                    return False
        # if there are open brackets in the stack without a closing bracket
        return not stack

if __name__ == "__main__":
    sol = Solution()
    assert sol.ValidParentheses("") == True
    assert sol.ValidParentheses("[({})]") == True
    assert sol.ValidParentheses("(]])") == False
    print("All tests passed!")

