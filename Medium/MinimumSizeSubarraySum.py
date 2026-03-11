'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Logic: Use sliding window logic by keeping a left pointer and minimum_sum variable. Increment the left pointer when you find the total
is >= to the target
Time: O(n)
Space: O(n)
'''

class Solution:
    def MinimumSize(self, target: int, nums: list[int]) -> int:
        min_sum = float('inf') # start at infinity so any valid window beats it
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_sum = min(min_sum, right-left+1)
                total -= nums[left]
                left += 1
        return 0 if min_sum == float('inf') else min_sum
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.MinimumSize(7, [2,3,1,2,4,3]))
