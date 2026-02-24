'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true

Pattern: Recursion on binary tree
Time: O(min(n, m)) - nodes/size of trees
Space: O(min(h1, h2)) - height of trees
'''

# common pattern for binary tree initialization. Non-binary tree would use a list named children instead of left and right.
class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def SameTree(self, p, q):
        # basecases:
        # if both empty return True
        if not p and not q:
            return True
        
        # make sure p and q are both true and checks if their values are equal
        if p and q and p.val == q.val:
            # recurse and return true if values continue to equal each other
            return self.SameTree(p.left, q.left) and self.SameTree(p.right, q.right)
        return False
 
if __name__ == '__main__':
    sol = Solution()

# Build tree p: 1 -> 2, 3
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Build tree q: 1 -> 2, 3
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(sol.SameTree(p, q))  # True

# Different tree
q2 = TreeNode(1)
q2.left = TreeNode(2)
q2.right = TreeNode(4)  # Different value - False

print(sol.SameTree(p, q2))
        

