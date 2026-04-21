'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O
(
1
)
O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Logic: Can do this 2 ways: 1. Use two stacks with one of them holding the min value seen.
2. use one stack and store as tuple with curr and min

'''
class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        if not self.stack:
            self.stack.append((val,val))
        else:
            curr_min = min(val, self.stack[-1][1])
            self.stack.append((val, curr_min))

    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    def getMin(self):
        return self.stack[-1][1]

if __name__ == "__main__":
    sol = MinStack()

    print(sol.push(5))
    print(sol.push(7))
    print(sol.getMin())
