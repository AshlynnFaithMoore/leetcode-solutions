'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Logic: Use a set to hold values already seen and check the set for each value in the list
'''
class Solution:
    def ContainsDup(self, nums: list[int]):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
if __name__ == '__main__':
    sol = Solution()
    assert sol.ContainsDup([1,2,3,3]) == True
    print("Passed!")