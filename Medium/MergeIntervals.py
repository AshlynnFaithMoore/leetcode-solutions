'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

Logic: two pointers kinda
Time: O(nlogn)
Space: O(n)
'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start value
        intervals.sort()
        merged = []
        prev = intervals[0]
        # walk thru intervals
        for interval in range(1, len(intervals)):
        # compare the current start against lists end value
            if intervals[interval][0] <= prev[1]:
                
        # If overlap → merge using max for the end value 
                prev[1] = max(prev[1], intervals[interval][1])
        #If no overlap → just append 
            else:
                merged.append(prev)
                prev = intervals[interval]
        merged.append(prev)
        return merged