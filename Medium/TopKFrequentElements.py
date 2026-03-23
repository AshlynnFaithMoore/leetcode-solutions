'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

Logic: "K frequent" usually means use a heap so we are going to use a max heap on the frequencies of the
elements in the list. Return the top k.

Time: 
Space: 
'''

import heapq

class Solution:
    def TopK(self, nums: list[int], k: int) -> list[int]:
        # count frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        # intialize heap and walk through frequencies
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        # initialize a result list and only append top k
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
if __name__ in "__main__":
    sol = Solution()
    assert sol.TopK([1,1,1,2,2,3], 2)
    assert sol.TopK([1,2,1,2,3,1,3,2], 2)
    print("Testcases passed!")

