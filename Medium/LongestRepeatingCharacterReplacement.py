'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Logic: Sliding window with a frequency hashmap. COMMON PATTERN - keeping track of the window length -> right - left + 1
Time: O(n)
Space: O(n)
'''
from math import inf


class Solution:
    def longestRepeating(self, s:str, k:int) -> int:
        # variables to keep track of: left pointer, max_count, freq_hash, result variable
        left = 0
        max_count = float(-inf)
        freq_hash = {}
        res = 0

        # walk thru string and add to freq_hash/update max_count
        for right in range(len(s)):
            freq_hash[s[right]] = freq_hash.get(s[right], 0) + 1
            max_count = max(max_count, freq_hash[s[right]])

            # while we have an invalid window -> window length - max is > k
            while (left - right + 1) - max_count > k:
                # remove left from our freq_hash and move it forward to shrink the window
                freq_hash[s[left]] -= 1
                left += 1

            # Update result with current valid window size
            res = max(res, right-left + 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    assert sol.longestRepeating('ABAB', 2) == 4
    print("Testcase passed!")
