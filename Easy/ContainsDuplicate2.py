'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Logic: Sliding window. The description is confusing, it's trying to say that the 2 values equal each other AND are at most 
k distance away from each other. Monitor the window size and only add the right pointer to the set.

Time: O(n)
Space: O(k) bc we store at most k values at a time

'''
class Solution:
    def containsDup(self, nums: list[int], k: int) -> bool:
        seen = set()
        left = 0
        # initialize left pointer value in seen
        seen.add(nums[left])
        for right in range(1, len(nums)):
            # check window length is valid
            if right - left > k:
                # if invalid window, remove left and walk it forward to shrink
                seen.remove(nums[left])
                left += 1
            # check right val in seen
            if nums[right] in seen:
                return True
        # add right value no matter what
            seen.add(nums[right])
        return False
    
if __name__ == '__main__':
    sol = Solution()
    assert sol.containsDup([1,2,3,1,2,3], 2) == False
    print("Testcase 1 passed!")
