class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        i = 0
        
        while i < len(height):
            # If stack is empty or current height is smaller/equal
            if len(stack) == 0 or height[stack[-1]] >= height[i]:
                stack.append(i)
                i += 1
            else:
                # Pop from stack and calculate trapped water
                x = stack.pop()
                
                if len(stack) != 0:
                    # Calculate trapped water
                    min_height = min(height[stack[-1]], height[i])
                    distance = i - stack[-1] - 1
                    water += distance * (min_height - height[x])
        
        return water

        