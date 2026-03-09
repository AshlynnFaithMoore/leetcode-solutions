'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3

Logic: Can use DFS or BFS and can use iterative or recursive. Easiest to write is Recursive DFS.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def MaxDepth(self, root: TreeNode):
        if root is None:
            return 0

        return 1 + max(self.MaxDepth(root.left), self.MaxDepth(root.right))


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)

    print(sol.MaxDepth(root))  # Expected: 2
    
