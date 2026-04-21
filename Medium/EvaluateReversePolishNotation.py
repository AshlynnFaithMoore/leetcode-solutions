'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

Logic: Two ways: 1. keep 2 variables that get pushed/popped from stack and have operations done
2. Make a method that maps the symbol to the math function

'''
class Solution:
    def evalRPN(self, tokens):
        ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)  # RPN usually truncates toward 0
        }

        stack = []

        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]
    
if __name__ in "__main__":
    sol = Solution()
    print(sol.evalRPN(["1","2","+","3","*","4","-"]))
