'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Pattern: Recursion on binary tree
Time: O(n)
Space: O(h)

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def InvertBinaryTree(self, root):
        # basecase
        if not root:
            return root
        
        # switch pointers then invert subtrees
        root.right, root.left = root.left, root.right
        self.InvertBinaryTree(root.right)
        self.InvertBinaryTree(root.left)

        return root
    
if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(2)
    root.right = TreeNode(5)
    root.left = TreeNode(4)

    print("The result: ")
    print(sol.InvertBinaryTree(root))