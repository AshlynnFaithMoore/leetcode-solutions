'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Pattern: Binary Search
Time/Space: O(logn), O(1)
'''
class Solution:
    def BinarySearch(self, nums: list[int], target: int) -> int:
        # define left and right pointers
        left, right = 0, len(nums) - 1

        # create a while loop to stay in bounds
        while left <= right:
            # calculate middle
            mid = left + (right - left) // 2
            # if target was the middle return the mid index
            if nums[mid] == target:
                return mid
            # if target is less than mid we need to focus on left side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
if __name__ == '__main__':
    sol = Solution()
    assert sol.BinarySearch([-1,0,1,2,3,4,5,6], 5) == 6
    print('test passed!')
