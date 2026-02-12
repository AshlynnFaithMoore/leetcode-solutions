'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Pattern: Frequency Hashmap
Time: O(n)
Space: O(k) where k is unique numbers

'''
class Solution:
    def ValidAnagram(self, s:str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] = freq.get(char, 0) - 1
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.ValidAnagram("abcd", "dcba") == True
    print("test passed!")

