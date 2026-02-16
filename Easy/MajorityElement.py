'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Pattern: Boyer-Moore Voting Algo or Freqhash
'''


class Solution:
    def MajorityElement(self, nums):
        # find majority to compare to
        majority = (len(nums)//2) + 1
        # find frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # walk through the items
        for i, val in freq.items():
            if val >= majority:
                return i




if __name__ == "__main__":
    sol = Solution()
    assert sol.MajorityElement([2,3,2]) == 2
    assert sol.MajorityElement([1,2,3,3,3,3,4]) == 3
    print("all tests passed")