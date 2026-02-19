'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Pattern: Backtracking
'''
class Solution:
    def CombinationSum(self, candidates, target):
        # make a result list and a current list
        res = []
        curr = []
        # make a backtracking function
        def backtrack(index, remaining):
            # basecase #1 : remaining == 0 then we can push to result
            if remaining == 0:
                # make a copy
                res.append(curr[:])
                return
            # Basecase 2: We went over the target and this path is invalid
            if remaining < 0:
                return
            # Basecase 3: We considered all candidates and nothing worked
            if index == len(candidates):
                return
            # Recursive case: Make decisions
            curr.append(candidates[index]) # add to combination
            backtrack(index, remaining - candidates[index])

            # We're done exploring paths with this number in this position
            # Remove it so we can try other options
            curr.pop()

            # skip current candidate and try next one
            backtrack(index + 1, remaining)
        backtrack(0, target)
        return res
if __name__ == "__main__":
    sol = Solution()
    assert sol.CombinationSum([2,3,6,7], 7) == [[2,2,3],[7]]
    print("Passed Test!")
