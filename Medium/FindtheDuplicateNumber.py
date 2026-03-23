'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

Logic: Since you can't sort or use any extra space you have to do cycle detection. Similar to how we detect the middle or cycles 
in a linked list, except this is for a regular list.
Time: O(n)
Space: O(1)
'''

class Solution:
    def FindDup(self, nums: list[list[int]]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow] #walk one step
            fast = nums[nums[fast]] #walk two steps
            if slow == fast: #we found the dup
                break
        
        slow2 = nums[0]
        while slow != slow2: #compare known dup
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
