'''
Docstring for Easy.TwoSum

Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Time Complexity: O(n)
Space Complexity: O(n)
'''
class Solution:
    def TwoSum(self, nums: list[int], target: int) -> list[int]:
        # defining an empty hash to store number as key and its index as value
        seen = {}
        # walk thru nums, getting the key and value for the hash
        for i, val in enumerate(nums):
            # find the missing value
            missing = target - val
            # check if already in hash
            if missing in seen:
                return [seen[missing], i]
            seen[val] = i
        return []
    
if __name__ == "__main__":
    # Create an instance to test
    sol = Solution()
    assert sol.TwoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.TwoSum([3, 2, 4], 6) == [1, 2]
    assert sol.TwoSum([3, 3], 6) == [0, 1]
    print("All tests passed!")
                




