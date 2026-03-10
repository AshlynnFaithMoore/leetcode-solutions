'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Logic: Walk through the list and sort the individual strings to use as a hashkey. Create a list of values that match the key then return 
all values as a list.

Time: O(nlogn)
Space: O(n)

'''


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #basecase
        if len(strs) == 0:
            return [[""]]
        
        # create empty hashmap
        seen = {}

        # walk through each string/word in list
        for word in strs:
            sortedword = ''.join(sorted(word))
            # check if sortedword is a key in the hashmap, if so append the word
            if sortedword in seen:
                seen[sortedword].append(word)
            else: # if not in hashmap create the key and add word in list
                seen[sortedword] = [word]
        
        return list(seen.values())

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    


