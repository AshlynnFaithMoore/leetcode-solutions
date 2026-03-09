'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def ReverseLinkedList(head: Optional[ListNode]):
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def PrintLL(head: Optional[ListNode]):
        curr = head

        while curr:
            print(curr.val, end="->")
            curr = curr.next

    
if __name__ == '__main__':
    sol = Solution
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    sol.PrintLL(head)

    head = sol.ReverseLinkedList(head)
    print()
    sol.PrintLL(head)
    

