'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Pattern: Two Pointers + Dummy Node
Time: O(n + m) where n, m are lengths of the lists
Space: O(1) - only using pointers, reusing existing nodes
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def MergeTwoSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a current node and a dummy node that points to head
        curr = dummy = ListNode(0)
        # check to make sure one list isn't empty
        if list1 is None and list2:
            return list2
        elif list2 is None and list1:
            return list1
        # have curr point to smallest 
        while list1 and list2:
            print("l1 val", list1.val)
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        # add remaining assuming lists are not even with each other
        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1
        print(dummy.next)
        return dummy.next
    
# Quick helper to make linked lists from arrays
def make_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Quick helper to convert linked list back to array
def to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    sol = Solution()
    
    # Test cases
    assert to_array(sol.MergeTwoSortedLists(make_list([1,2,4]), make_list([1,3,4]))) == [1,1,2,3,4,4]
    assert to_array(sol.MergeTwoSortedLists(make_list([]), make_list([]))) == []
    assert to_array(sol.MergeTwoSortedLists(make_list([]), make_list([0]))) == [0]
    
    print("All tests passed!")

        