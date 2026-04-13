'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Logic: Duplicates matter and we need fast lookups. Put the list into a set, walk through and check each number
to see if it is the start of the sequence. If so, begin counting the length and compare at the end to find
the max length to return.

Time: O(n)
Space: O(n)

'''

class Solution:
    def LongestConsecutive(self, nums):
        seen = set(nums)
        length = 0
        max_length = 0
        for num in nums:
            if (num-1) not in seen:
                length = 1

                while (num + length) in seen:
                    length += 1
                
                max_length = max(max_length, length)
        return max_length

if __name__ == '__main__':
    sol = Solution()
    print(sol.LongestConsecutive([2,20,4,10,3,4,5]))