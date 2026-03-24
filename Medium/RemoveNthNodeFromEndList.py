'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Logic: Use fast/slow pointers. start an n sized gap between the fast and slow pointer. Then move both pointers 
until fast reaches the end. Slow will be at the node before the node to skip so you can just skip it then.
Time: O(n)
Space: O(1)

'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def RemoveNthNode(self, head: Optional[ListNode], n: int):
        fast = head
        dummy = ListNode(0, head)
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
    
if __name__ == '__main__':
    sol = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    result = sol.RemoveNthNode(head, 2)

    # Print result
    while result:
        print(result.val, end=" → ")
        result = result.next