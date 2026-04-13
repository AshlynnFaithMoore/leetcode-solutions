'''
You are given an integer array heights where heights[i] represents the height of the 
ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]

Output: 36

Logic: Calculate the current area using the minimum value as the limiting factor. Then get the max area and move left/right 
pointers by minimum value.
Time: O(n)
Space: O(1)

'''
class Solution:
    def ContainerMostWater(self, heights):
        left, right = 0, len(heights)-1
        max_area = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == '__main__':
    sol = Solution()
    print(sol.ContainerMostWater([1,7,2,5,4,7,3,6]))