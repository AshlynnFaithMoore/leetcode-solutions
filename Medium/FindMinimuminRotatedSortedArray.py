'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0
Example 3:

Input: nums = [4,5,6,7]

Output: 4

Logic: We know that one half was sorted while the other half was not, in other words there will be one unsorted side
Use binary search to compare right to mid and continue upadting mid until they equal each other.
Time: O(logn)
Space: O(1)

'''
class Solution:
    def FindMin(self, nums:list[int]) -> int:
        left,right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
    
if __name__ == '__main__':
    sol = Solution()
    assert sol.FindMin([3,4,5,6,1,2]) == 1
    assert sol.FindMin([4,5,6,7]) == 4
    print("passed all testcases!")