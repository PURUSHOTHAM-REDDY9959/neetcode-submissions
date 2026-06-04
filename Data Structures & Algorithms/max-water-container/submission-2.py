class Solution:
    def maxArea(self, heights):
        l = 0                      # left pointer (start)
        r = len(heights) - 1       # right pointer (end)
        ans = 0                    # to store maximum area

        while l < r:
            # width between two bars
            width = r - l
            
            # height is the smaller of two bars
            height = min(heights[l], heights[r])
            
            # calculate area
            area = width * height
            
            # update maximum area
            ans = max(ans, area)

            # move the pointer with smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans
