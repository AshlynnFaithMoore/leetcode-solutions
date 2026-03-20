'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Logic: Take the first element and shrink it until it fits the next word. Continue this until 
we've reached the end of the list. return 
Time:
Space:
'''
from typing import List
class Solution:
    def LongestCommonPrefix(self, strs: List[str]) -> str:
        # keep the first word in a variable
        prefix = strs[0]
        # take the length of the first word
        prefix_length = len(prefix)
        # walk through the rest of the strings
        for word in strs[1:]:
            # while prefix != word
            while prefix != word[0:prefix_length]:
                prefix_length -= 1
                if prefix_length == 0:
                    return ""

                prefix = prefix[0:prefix_length]

        return prefix

if __name__ == '__main__':
    sol = Solution()
    assert sol.LongestCommonPrefix(["flower","flow","flight"]) == 'fl'
    print("Testcase passed!")