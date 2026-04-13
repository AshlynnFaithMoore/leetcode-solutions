'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Logic: pre-process data to make it alphanumeric and all the same case. If the values dont equal each other at any point
return false, else keep iterating and return true.
Time: O(n)
Space: O(1)

'''

class Solution:
    def ValidPalindrome(self, s):
        s = s.lower()
        left, right = 0, len(s)-1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.ValidPalindrome("Was it a car or a cat I saw?"))