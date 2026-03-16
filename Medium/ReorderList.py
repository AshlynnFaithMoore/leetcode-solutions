'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Logic: Find the middle of the list, seperate the halves, reverse the last half, reorder
Time: O(n)
Space: O(1)
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        # find middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # sepearate the list at the halfway mark
        second_list = slow.next
        slow.next = None

        # reverse last half
        prev = None
        while second_list:
            next_node = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = next_node

        # rebuild list
        first, second = head, prev  # prev is now the head of reversed second half
        while second:
        # merge
            temp1 = first.next 
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    def printList(head):
        while head:
            print(head.val, end=" -> " if head.next else "\n")
            head = head.next

    sol.reorderList(head)
    printList(head)


            
